from functions import plot_compute_times
times_vec = [5,8,10]
cpu_vec = [1,3,5]
com_vec = ['Serial','Parallel','Dask']
with open('benchmarks.csv','w') as f:
    for cpu,com,time in zip(cpu_vec,com_vec,times_vec):
        f.write(com + ", " + str(cpu) + ", " + str(time) + '\n')
plot_compute_times(cpu_vec,times_vec,com_vec,png_name='test')

