mask_dask = ma.masked_less(cir_mat, 13)
print("Lazy Dask array properties are: \n{}".format(mask_dask))
mask_dask = mask_dask.compute().mask
print("The final mask: \n{}".format(mask_dask))
