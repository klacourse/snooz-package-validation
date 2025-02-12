"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    SumoExampleV1
    Class to detect spindles based on the SUMO algorithm
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import numpy as np
import sys, os
import time
import pandas as pd

# Comment out the following imports if no need to plot the spindles
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")

# # Get the directory of the current script
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # Add the parent directory to the Python path
# sys.path.append(current_dir)

from .get_model import get_model
from sumo.config import Config
from sumo.data import spindle_vect_to_indices
from .butter_filter import butter_bandpass_filter, downsample
# from .segment_data import segment_epochs
from scipy.stats import zscore
import torch
from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl
from CEAMSModules.EventReader import manage_events

# Set environment variables for evaluation timeout
os.environ['PYDEVD_WARN_EVALUATION_TIMEOUT'] = '10'
os.environ['PYDEVD_UNBLOCK_THREADS_TIMEOUT'] = '5'
os.environ['PYDEVD_THREAD_DUMP_ON_WARN_EVALUATION_TIMEOUT'] = 'true'
os.environ['PYDEVD_INTERRUPT_THREAD_TIMEOUT'] = '5'

DEBUG = False
plot = False
plot_len = 8  # Length of the window to plot around the spindle in seconds (any even number between 2 and 30) 

class SimpleDataset(Dataset):
    def __init__(self, data_vectors):
        super(SimpleDataset, self).__init__()

        self.data = data_vectors

    def __len__(self) -> int:
        return len(self.data)

    @staticmethod
    def preprocess(data):
        return zscore(data)

    def __getitem__(self, idx):
        data = self.preprocess(self.data[idx])
        return torch.from_numpy(data).float(), torch.zeros(0)

class SumoExampleV1(SciNode):
    """
    Class to detect spindles based on the SUMO algorithm

    Parameters
    ----------
        signals : List of SignalModel
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original             
        event_group : String
            List of Event group to filter separated by comma (discard too long, short)
        event_name : String
            List of Event name to filter separated by comma (discard too long, short)
        artifact_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Selected events list for artifacts.
        
    Returns
    -------
        events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events list for spindle detections.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SumoExampleV1 """
        super().__init__(**kwargs)
        if DEBUG: print('SumoExampleV1.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('event_group',self)
        InputPlug('event_name',self)
        InputPlug('artifact_events',self)
        
        # Output plugs
        OutputPlug('events',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0
 
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signals, event_group, event_name, artifact_events):
        """
        Function to detect spindles based on the SUMO algorithm.

        Parameters
        ----------
            signals : List of SignalModel
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original

            event_group : String
                List of Event group to filter separated by comma (discard too long, short)

            event_name : String
                List of Event name to filter separated by comma (discard too long, short)

            artifact_events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Selected events list for artifacts.

            

        Returns
        -------
            events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Events list for spindle detections.
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        # raise NodeInputException(self.identifier, "my_input", \
        #        f"SumoExample this input is wrong.")
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"SpindleDetectorSUMO this input is empty, no signals no spindles.")     
        if isinstance(event_group, str) and event_group=='':
            raise NodeInputException(self.identifier, "event_group", \
                f"SpindleDetectorSUMO this input is empty, no event_group no spindles.")
        if isinstance(event_name, str) and event_name=='':
            raise NodeInputException(self.identifier, "event_name", \
                f"SpindleDetectorSUMO this input is empty, no event_name no spindles.")
        if not isinstance(artifact_events, pd.DataFrame) and not artifact_events=='':
            raise NodeInputException(self.identifier, "artifact_events", \
                f"SpindleDetectorSUMO this input is a {type(artifact_events)}, it is expected to be a Pandas DataFrame.")            

        # Raise NodeRuntimeException if there is a critical error during runtime. 
        # This will usually be a user error, a file that can't be read due to security reason,
        # a parameter that is out of bound, etc. This exception will stop and skip the current
        # process but will not stop the followin iterations if a master node is not done.
        # Once the master node is completed, a dialog will appear to show all NodeRuntimeException
        # to the user.
        #
        # Set the iteration_identifier if this module is a master node.
        # This will be used to identify the problematic iteration if a runtime exception occurs
        # in any module during this process. For example, a master node that reads one file at a 
        # could set the identifier to the name of the file.
        # self.iteration_identifier = current_filename
        #
        # Iteration count and counter are used to show a progress bar in percent.
        # Update these when creating a master node to properly show the progress 
        # for each iteration. This is optional and can be ignored but it's a good practice
        # to do for your users.
        #self.iteration_count = the total amout of iteration to make
        #self.iteration_counter = the current iteration number

        # filter and downsample
        signals_original = signals.copy()
        sample_rate = signals[0].sample_rate
        resample_rate = 100
        signals = [downsample(butter_bandpass_filter(x.samples, 0.3, 30.0, sample_rate, 10), sample_rate, resample_rate) for x in signals]
        
        # for signal in signals:  # I think there is no need to loop over the signals bc of having dataloader
        #     if DEBUG: 
        #         print(f"SpindleDetectorA7.compute signal {i_signal} starts at {time.strftime('%H:%M:%S', time.gmtime(signal.start_time))}")
        #         i_signal += 1

        #     data = signal.samples
            
            # filter and downsample (already done above on all the epochs together)
            # sample_rate = signal.sample_rate
            # resample_rate = 100
            # data = downsample(butter_bandpass_filter(data, 0.3, 30.0, sample_rate, 10), sample_rate, resample_rate)

            # set up the model


            # predict the spindles

        # Create a dataset and dataloader
        dataset = SimpleDataset(signals)
        dataloader = DataLoader(dataset, num_workers=3, persistent_workers=True)

        # Set up the model and its config
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = current_dir + '/final.ckpt'  # added by me
        config = Config('predict', create_dirs=False)

        model = get_model(model_path, config)
        trainer = pl.Trainer(num_sanity_val_steps=0, logger=False)
        # gpu = torch.cuda.is_available()  # added by me
        # trainer = pl.Trainer(gpus=int(gpu), num_sanity_val_steps=0, logger=False)

        # Predict the spindles
        predictions = trainer.predict(model, dataloader)  # 0/1 label for each data point of each segment (takes ~50 sec)
        # predictions = predictions.detach().cpu().numpy()  # if written in loop 
        predictions = [pred.detach().cpu().numpy() for pred in predictions]

        # get spindle indices for one sample segment
        # pred = predictions[0].flatten()
        # spindle_ind = spindle_vect_to_indices(predictions)  # fix error add a loop over segments

        # Compute spindle indices list (loop method)
        # spindle_indices_list = []
        # spindle_counts = []
        # for pred in predictions:
        #     pred_flattened = pred.flatten()  # Ensure it's 1D
        #     spindle_indices = spindle_vect_to_indices(pred_flattened)
        #     spindle_count = spindle_indices.shape[0]  # Number of spindles
        #     if spindle_indices.size > 0:  # Only add if not empty
        #         spindle_indices_list.append(spindle_indices)
        #         spindle_counts.append(spindle_count)

        # Compute spindle indices list (list comprehension method, faster, less memory)
        spindle_indices_list = [spindle_vect_to_indices(pred.flatten()) for pred in predictions]  # indices of spindles within each segment
        
        # Compute spindle counts (keeping empty elements as 0)
        spindle_counts = [spindle.shape[0] if spindle.size > 0 else 0 for spindle in spindle_indices_list]

        total_spindles = sum(spindle_counts)  # Total spindles across all signals
        if DEBUG:
            print(f"Total number of spindles detected: {total_spindles}")

        # Find indices where the spindle indices list is not empty
        non_empty_indices = [i for i, spindles in enumerate(spindle_indices_list) if spindles.size > 0]

        # Plot/save the spindles on the first 5 segments containing spindles
        if plot:
            # Find the first segments with spindles
            first_spindle_inds = []
            for i, spindle_indices in enumerate(spindle_indices_list):
                if spindle_indices.size > 0 and len(first_spindle_inds) < 10: 
                    first_spindle_inds.append(i)
            # Extract the corresponding signals
            signal_to_plot, spindle_ind = [], []
            for j in range(len(first_spindle_inds)):
                signal_to_plot.append(signals[first_spindle_inds[j]].flatten())
                spindle_ind.append(spindle_indices_list[first_spindle_inds[j]])

            if plot_len == 30:
                for i, (signal, ind) in enumerate(zip(signal_to_plot, spindle_ind)):
                    # Plot the signal
                    plt.figure(figsize=(12, 4))
                    plt.plot(signal, label="EEG Signal", color="blue")
                    # Highlight the spindle regions
                    for start, stop in ind:
                        plt.axvspan(start, stop, color='red', alpha=0.3, label="Spindle" if start == ind[0, 0] else "")
                    plt.xlabel("Time (samples)")
                    plt.ylabel("Amplitude")
                    plt.title(f"EEG Segment {first_spindle_inds[i]} with Spindles Highlighted")
                    plt.legend()
                    plt.savefig(f"eeg_spindle_plot_{i}.png", dpi=300, bbox_inches="tight")
                    plt.close()
            else:
                matplotlib.use("Agg")
                for i, (signal, ind) in enumerate(zip(signal_to_plot, spindle_ind)):
                    # Find the center of the spindle segment
                    segment_center = (ind[0][0] + ind[0][1]) // 2
                    # Define the window for 8 seconds around the spindle
                    window_start = max(segment_center - int(plot_len/2) * resample_rate, 0)
                    window_stop = min(segment_center + int(plot_len/2) * resample_rate, len(signal))
                    # Extract the signal within this window
                    time_axis = np.arange(window_start, window_stop) / resample_rate
                    signal_segment = signal[window_start:window_stop]
                    # Plot the extracted window
                    plt.figure(figsize=(12, 4))
                    plt.plot(time_axis, signal_segment, label="EEG Signal", color="blue")
                    # Highlight spindle regions within this window
                    for start, stop in ind:
                        if stop >= window_start and start <= window_stop:
                            plt.axvspan(start / resample_rate, stop / resample_rate, color='red', alpha=0.3, label="Spindle" if start == ind[0, 0] else "")
                    plt.xlabel("Time (seconds)")
                    plt.ylabel("Amplitude")
                    plt.title(f"EEG Segment {first_spindle_inds[i]} with Spindles Highlighted ({plot_len}s Window)")
                    plt.legend()
                    plt.savefig(f"eeg_spindle_{plot_len}s_window_{i}.png", dpi=300, bbox_inches="tight")
                    plt.close()  # Close to free memory

        # Index to time
        spindle_time_list = [[(start / resample_rate, stop / resample_rate) for start, stop in spindle_indices] for spindle_indices in spindle_indices_list]
        
        # Add the event_name and the channel label to the events list
        event_lst = []
        for i, spindle_time in enumerate(spindle_time_list):
            for start, stop in spindle_time:
                event_lst.append((event_group, event_name, signals_original[i].start_time+start, stop-start, signals_original[i].channel))
        
        # Create a pandas dataframe of events (each row is an event) for the current pds
        events_df = manage_events.create_event_dataframe(event_lst)

        # Raise the runtime exception
        # raise NodeRuntimeException(self.identifier, "files", \
        #        f"Some file could not be open.")

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{len(events_df)} spindles  were found.")

        return {
            'events': events_df
        }