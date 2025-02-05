# numpy taands for numerical python 
import numpy as np
b = [1,2,3,4,5,6]
a = np.array(b)
print(b)
print(type(b))
print(a)
print(type(a))

a_mul = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]) # multi dimenisonal array

print(a_mul[0,0])
print(a_mul[0,1])
print(a_mul[0,2])
print(a_mul[1,0])
print(a_mul[1,1])
print(a_mul[1,2])
print(a_mul[3,2])

print(a_mul.shape) # output (4,3) 1 list contain 4 list each has 3 element
print(a_mul.ndim)
print(a_mul.size) # tell total number of elements 
b_mul =np.array([
    [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
    ],
    [
        [2,2,2,2],
        [2,2,2,2],
        [2,2,2,2], 
        [2,2,2,2]
    ]
])

print(b_mul.shape) # output (2,4,4) 2 list conatin 4 list each each list has 4 elements
print(b_mul.ndim)
print(b_mul.size)
print(b_mul.dtype)
