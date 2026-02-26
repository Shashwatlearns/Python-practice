import numpy as np
array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']]
                ,[['J','K','L'],['M','N','O'],['P','Q','R']]
                ,[['S','T','U'],['V','W','X'],['Y','Z','_']]])
print(type(array))

print(array.ndim)

print(array.shape)

print(array.size)

print(array[0][0][0])           # chain indexing, not recommended as it is slower

print(array[0,0,0])             # multidimensional indexing, recommended way of indexing

word= array[1,1,0]+array[0,1,1]+array[1,1,2]+array[2,1,1]
print(word)