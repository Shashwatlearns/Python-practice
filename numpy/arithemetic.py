import numpy as np
array_1=np.array([1,2,3,4])

#Scalar

print(array_1+1)
print(array_1-5)
print(array_1*4)
print(array_1/2)
print(array_1**3)

#Vector

array_2=np.array([1.01,4.5,3.5,6.78])
print(np.sqrt(array_2))
print(np.round(array_2))
print(np.sqrt(array_2))
print(np.ceil(array_2))
print(np.floor(array_2))

#Constant

print(np.pi)
print(np.e)
print(np.euler_gamma)
print(np.inf)

#element

array1=np.array([1,2,3])
array2=np.array([4,5,6])
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)

#Comparison
print(array1 > array2)
print(array1 < array2)
print(array1 == array2)
print(array1 != array2)

scores=np.array([90,80,70,60,20,0])  
print(scores > 80)
print(scores < 80)
print(scores == 80)
print(scores != 80)
scores[scores > 80] = 100
print(scores)