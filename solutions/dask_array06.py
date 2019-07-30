cir_mat = da.sqrt(u_mat2**2 + v_mat2**2)
fig, axis = plt.subplots()
#axis.imshow(cir_mat) or
usid.plot_utils.plot_map(axis, cir_mat, show_cbar=True)
cir_mat
