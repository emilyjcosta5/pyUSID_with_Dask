x = stem_4d_dask[:,:,32,32]
x = x.astype('float32')
fig, axis = plt.subplots()
axis.imshow(x)
