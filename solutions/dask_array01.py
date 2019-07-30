y = stem_4d_dask[1,1]
y = y.astype('float32')
fig, axis = plt.subplots(ncols=2)
axis[0].imshow(x)
axis[1].imshow(y)
