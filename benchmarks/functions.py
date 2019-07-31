from __future__ import division, print_function, absolute_import, unicode_literals

# The package for accessing files in directories, etc.:
import os

# Warning package in case something goes wrong
from warnings import warn
import subprocess
#from dask.diagnostics import Profiler, ResourceProfiler, visualize
import dask.array as da


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
# Package for downloading online files:
try:
    # This package is not part of anaconda and may need to be installed.
    import wget
except ImportError:
    warn('wget not found.  Will install with pip.')
    import pip
    install(wget)
    import wget

# The mathematical computation package:
import numpy as np
import dask
from dask.distributed import Client, LocalCluster
import dask.array as da

# The package used for creating and manipulating HDF5 files:
import h5py

# Packages for plotting:
import matplotlib.pyplot as plt

# Parallel computation library:
try:
    import joblib
except ImportError:
    warn('joblib not found.  Will install with pip.')
    import pip
    install('joblib')
    import joblib

# Timing
import time

# A handy python utility that allows us to preconfigure parts of a function
from functools import partial

# Finally import pyUSID:
try:
    import pyUSID as usid
except ImportError:
    warn('pyUSID not found.  Will install with pip.')
    import pip
    install('pyUSID')
    import pyUSID as usid
    

# import the scientific function:
import sys
sys.path.append('./supporting_docs/')
from peak_finding import find_all_peaks

def get_main(url,h5_path='temp.h5'):
    if os.path.exists(h5_path):
        os.remove(h5_path)
    _ = wget.download(url, h5_path, bar=None)
    # Open the file in read-only mode
    h5_file = h5py.File(h5_path, mode='r')
    # Get handle to the the raw data
    h5_meas_grp = h5_file['Measurement_000']
    # Accessing the dataset of interest:
    h5_main = usid.USIDataset(h5_meas_grp['Channel_000/Raw_Data'])
    num_rows, num_cols = h5_main.pos_dim_sizes
    return h5_main

def test_peak_finding(h5_main):
    row_ind, col_ind = 110, 25
    pixel_ind = col_ind + row_ind * num_cols
    spectra = h5_main[pixel_ind]

    peak_inds = find_all_peaks(spectra, [20, 60], num_steps=30)
    
    fig, axis = plt.subplots()
    axis.scatter(np.arange(len(spectra)), np.abs(spectra), c='black')
    axis.axvline(peak_inds[0], color='r', linewidth=2)
    axis.set_ylim([0, 1.1 * np.max(np.abs(spectra))]);
    axis.set_title('find_all_peaks found peaks at index: {}'.format(peak_inds), fontsize=16)

def run_dask_compute(h5_main):
    raw_data = h5_main[()]
    #cpu_cores = int(cpu_cores/8)
    dask_raw_data = da.from_array(raw_data, chunks='auto')
    #cluster = LocalCluster(n_workers=cpu_cores/8)
    #client = Client(cluster, processes=True)
    #map = dask_raw_data.map_blocks(find_all_peaks, [20, 60], num_steps=30)
    #results = map.compute()
    client = Client(processes=False)
    L = client.map(find_all_peaks, dask_raw_data, width_bounds = [20, 60], num_steps=30)
    dask_results = client.gather(L)
    cores = client.ncores()
    client.close()
    return results

def run_serial_compute(h5_main):
    raw_data = h5_main([])
    serial_results = list()
    for vector in raw_data:
        serial_results.append(find_all_peaks(vector, [20, 60], num_steps=30))
    return serial_results

def run_parallel_compute(h5_main,cpu_cores=16): 
    raw_data = h5_main[()]
    args = [[20, 60]]
    kwargs = {'num_steps': 30}
    parallel_results = usid.parallel_compute(raw_data, find_all_peaks, cores=cpu_cores, func_args=args, func_kwargs=kwargs)
    return parallel_results

def plot_compute_times(cpu_vec,times_vec,com_vec,png_name='benchmarks'):
    colors = list()
    for com in com_vec:
        if com is 'Parallel': colors.append('blue')
        if com is 'Dask': colors.append('red')
        if com is 'Serial': colors.append('green')
    fig, axis = plt.subplots(figsize=(3.5, 3.5))
    axis.scatter(cpu_vec, times_vec, c=colors)
    axis.set_xlabel('CPU cores', fontsize=14)
    axis.set_ylabel('Compute time (sec)', fontsize=14)
    fig.tight_layout()
    plt.savefig('{}.png'.format(png_name))
