"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    SumoExampleV2
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
# import matplotlib
# import matplotlib.pyplot as plt
# matplotlib.use("Agg")

# # Get the directory of the current script
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # Add the parent directory to the Python path
# sys.path.append(current_dir)

# Get the absolute path of V1
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SumoExampleV1')))

from ..SumoExampleV1.get_model import get_model
from ..SumoExampleV1.sumo.config import Config
from ..SumoExampleV1.sumo.data import spindle_vect_to_indices
from ..SumoExampleV1.butter_filter import butter_bandpass_filter, butter_bandpass_filter_nan, downsample
# from ..SumoExampleV1.butter_filter import butter_bandpass_filter_nan  # use if nan values are present
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
sumo_input = "original"  # original or clean

class SimpleDataset(Dataset):
    def __init__(self, data_vectors, mean, std):
        super(SimpleDataset, self).__init__()

        self.data = data_vectors
        self.mean = mean
        self.std = std

    def __len__(self) -> int:
        return len(self.data)

    @staticmethod
    def preprocess(data, mean, std):
        return (data-mean)/std

    def __getitem__(self, idx):
        data = self.preprocess(self.data[idx], self.mean[idx], self.std[idx])
        return torch.from_numpy(data).float(), torch.zeros(0)
    
class SumoExampleV2(SciNode):
    """
    Class to detect spindles based on the SUMO algorithm

    Parameters
    ----------
        original_signals: List of SignalModel
            List of original signal (with artifacts) with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original         
        cleaned_signals: List of SignalModel
            List of cleaned signal (filtered, resampled, artifact-removed) with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original     
        norm_stat: List of Float
            List of cleaned signal statistics for normalization
            Contains mean and std for each channel
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
        """ Initialize module SumoExampleV2 """
        super().__init__(**kwargs)
        if DEBUG: print('SumoExampleV2.__init__')

        # Input plugs
        InputPlug('original_signals',self)
        InputPlug('cleaned_signals',self)
        InputPlug('norm_stat',self)
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
    
    def compute(self, original_signals,cleaned_signals,norm_stat,event_group,event_name,artifact_events):
        """
        TODO DESCRIPTION

        Parameters
        ----------
        original_signals: List of SignalModel
            List of original signal (with artifacts) with dictionary of channels with SignalModel with        
        cleaned_signals: List of SignalModel
            List of cleaned signal (filtered, resampled, artifact-removed) with dictionary of channels with SignalModel with 
        norm_stat: List of Float
            List of cleaned signal statistics for normalization
            Contains mean and std for each channel
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
            
        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Raise NodeInputException if an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        # raise NodeInputException(self.identifier, "my_input", \
        #        f"SumoExample this input is wrong.")
        if isinstance(original_signals, str) and original_signals=='':
            raise NodeInputException(self.identifier, "original_signals", \
                f"SpindleDetectorSUMO this input is empty, no signals no spindles.")   
        if isinstance(cleaned_signals, str) and cleaned_signals=='':
            raise NodeInputException(self.identifier, "cleaned_signals", \
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

        signals = original_signals.copy()
        sample_rate = signals[0].sample_rate
        resample_rate = 100

         # Filter and downsample
        signals = [downsample(butter_bandpass_filter(x.samples, 0.3, 30.0, sample_rate, 10), sample_rate, resample_rate) for x in signals]
        # cleaned_signals = [(butter_bandpass_filter_nan(x.samples, 0.3, 30.0, sample_rate, 10), sample_rate, resample_rate) for x in cleaned_signals]  # if not already done before sumo

        # Calculate mean and std on cleaned signals for normalization
        mean = [np.nanmean(x.samples) for x in cleaned_signals]
        std = [np.nanstd(x.samples) for x in cleaned_signals]

        # Release memory
        del cleaned_signals

        # Create a dataset and dataloader
        dataset = SimpleDataset(signals, mean, std)
        dataloader = DataLoader(dataset, num_workers=3, persistent_workers=True)

        # Set up the model and its config
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = current_dir + '/final.ckpt'  
        config = Config('predict', create_dirs=False)

        model = get_model(model_path, config)
        trainer = pl.Trainer(num_sanity_val_steps=0, logger=False)
 
        # Predict the spindles
        predictions = trainer.predict(model, dataloader)  # 0/1 label for each data point of each segment (takes ~50 sec)
        predictions = [pred.detach().cpu().numpy() for pred in predictions]

        # Compute spindle indices list (list comprehension method, faster, less memory)
        spindle_indices_list = [spindle_vect_to_indices(pred.flatten()) for pred in predictions]  # indices of spindles within each segment
        
        # Compute spindle counts (keeping empty elements as 0)
        spindle_counts = [spindle.shape[0] if spindle.size > 0 else 0 for spindle in spindle_indices_list]

        total_spindles = sum(spindle_counts)  # Total spindles across all signals
        if DEBUG:
            print(f"Total number of spindles detected: {total_spindles}")

        # Find indices where the spindle indices list is not empty
        non_empty_indices = [i for i, spindles in enumerate(spindle_indices_list) if spindles.size > 0]
        
        # Index to time
        spindle_time_list = [[(start / resample_rate, stop / resample_rate) for start, stop in spindle_indices] for spindle_indices in spindle_indices_list]
        
        # Add the event_name and the channel label to the events list
        event_lst = []
        for i, spindle_time in enumerate(spindle_time_list):
            for start, stop in spindle_time:
                event_lst.append((event_group, event_name, original_signals[i].start_time+start, stop-start, original_signals[i].channel))
        
        # Create a pandas dataframe of events (each row is an event) for the current pds
        events_df = manage_events.create_event_dataframe(event_lst)

        # Raise the runtime exception
        # raise NodeRuntimeException(self.identifier, "files", \
        #        f"Some file could not be open.")

        #
        #

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module does nothing.")

        return {
            'events': events_df
        }