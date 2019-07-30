from functions import *
import time

start = time.time()
h5_main = get_main('https://raw.githubusercontent.com/pycroscopy/pyUSID/master/data/BELine_0004.h5')

cores_vec = list()
time_vec = list()
com_vec = list()
cores = 16

parallel = time.time()
run_parallel_compute(h5_main,cpu_cores=cores)
time_vec.append(time.time()-parallel)
cores_vec.append(cores)
com_vec.append('Parallel')
print("Parallel compute finished in {}".format(time.time()-parallel))

dask = time.time()
cor = run_dask_compute(h5_main)
time_vec.append(time.time()-dask)
cores_vec.append(cor)
com_vec.append('Dask')
print("Dask compute finished in {}".format(time.time()-dask))

serial = time.time()
run_serial_compute(h5_main)
time_vec.append(time.time()-serial)
cores_vec.append(1)
com_vec.append('Serial')
print("Serial compute finished in {}".format(time.time()-serial))

plot_compute_times(cpu_vec,times_vec,com_vec,png_name='baseBenchmarks')

#some other benchmarks
'''
dask32 = time.time()
cor = run_dask_compute(h5_main)
time_vec.append(time.time()-dask32)
cores_vec.append(cor)
com_vec.append('Dask')
'''

para32 = time.time()
run_parallel_compute(h5_main, cpu_cores=32)
time_vec.append(time.time()-para32)
cores_vec.append(32)
com_vec.append('Parallel')
'''
dask8 = time.time()
run_dask_computer(h5_main, cpu_cores=8)
time_vec.append(time.time()-dask8)
cores_vec.append(8)
com_vec.append('Dask')
'''
para8 = time.time()
run_parallel_compute(h5_main, cpu_cores=8)
time_vec.append(time.time()-para8)
cores_vec.append(8)
com_vec.append('Parallel')

with open('benchmarks.csv','w') as f:
    for cpu,com,time in zip(cores_vec,com_vec,time_vec):
        f.write(com + ", " + str(cpu) + ", " + str(time) + '\n')
plot_compute_times(cpu_vec,times_vec,com_vec,png_name='benchmarks')
