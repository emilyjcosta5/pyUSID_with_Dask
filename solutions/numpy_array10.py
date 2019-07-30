ask1 = (13 < cir_mat) & (cir_mat < 25)
filtered1 = stem_4d*mask1
filtered1 = np.float32(filtered1)
b = np.mean(filtered1, axis=2)
c = np.mean(b, axis=2)
fig, axes = plt.subplots(ncols=2)
axes[0].imshow(c)
axes[1].imshow(np.float32(mask1))
