z = np.mean(stem_4d, axis=2)
a = np.mean(z, axis=2)
a = np.float32(a)
fig, axis = plt.subplots()
axis.imshow(a)
