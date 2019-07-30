mask1_dask = ma.masked_inside(cir_mat, 13, 25)
filtered1_dask = stem_4d_dask*mask1_dask
filtered1_dask = np.float32(filtered1)
b_dask = da.mean(filtered1_dask, axis=2, dtype='float32')
c_dask = da.mean(b_dask, axis=2, dtype='float32')
fig, axes = plt.subplots(ncols=2)
axes[0].imshow(c)
axes[1].imshow(mask1_dask)
