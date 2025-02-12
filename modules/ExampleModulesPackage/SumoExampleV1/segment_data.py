import numpy as np


def segment_epochs(eeg_epochs, sampling_rate, epoch_length=30):
    """
    Segments EEG epochs longer than the specified length into smaller 30-second epochs.

    Args:
        eeg_epochs (list of np.ndarray): Each element is an EEG signal array (variable length).
        sampling_rate (int): The sampling rate of the EEG signal (samples per second).
        epoch_length (int, optional): The target length for each segmented epoch in seconds. Default is 30.

    Returns:
        list of np.ndarray: A list where each element is exactly a 30-second EEG epoch.
    """
    segmented_epochs = []
    samples_per_epoch = sampling_rate * epoch_length  # Total samples in 30 sec
    
    for epoch in eeg_epochs:
        num_segments = len(epoch) // samples_per_epoch  # Number of 30-sec segments
        segmented_epochs.extend(np.split(epoch[:num_segments * samples_per_epoch], num_segments))  # Split into chunks
    
    return segmented_epochs