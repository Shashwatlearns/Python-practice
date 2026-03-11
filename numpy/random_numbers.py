import numpy as np

rng=np.random.default_rng(seed=3)
print(rng.integers(1,7,size=(6,6)))

np.random.seed(1)   
print(np.random.uniform(5,6,size=(3,3)))

rng=np.random.default_rng(seed=8)
array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

rng=np.random.default_rng()
fruits=np.array(['Apple','Banana','Cherry','Durian','Elderberry'])
fruit=rng.choice(fruits,size=(3,4))
print(fruit)