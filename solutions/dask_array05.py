test = da.random.randint(0, high=10, size=(5,5))
print(test)
'''
# This does not work:
mask = da.zeros_like(test)
mask[2:4, 2:4] = int(1)
'''b
mask = np.zeros((5, 5), dtype=np.uint16)
mask[2:4, 2:4] = 1
mask = da.from_array(mask, chunks='auto')
print(test.compute())
print(mask.compute())
print((test * mask).compute())
