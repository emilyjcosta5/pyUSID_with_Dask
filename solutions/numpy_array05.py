test = np.random.randint(0, high=10, size=(5,5))
mask = np.zeros((5, 5), dtype=np.uint16)
mask[2:4, 2:4] = 1
print(test)
print(mask)
print(test * mask)
