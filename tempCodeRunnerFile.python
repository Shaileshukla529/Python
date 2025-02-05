import numpy as np

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
zeros() function
Creates an array of all 0s with the given shape and dtype.
syntax : numpy.zeros(shape, dtype=None, order='C')
   shape → Tuple specifying the shape of the array (e.g., (rows, cols)).
   dtype (optional) → Specifies the data type (int, float, etc.). Default is float.
   order (optional) → Memory layout ('C' for row-major, 'F' for column-major).

'''
arr = np.zeros(5)
print(arr)

arr = np.zeros((5,4))
print(arr)

arr = np.zeros((5,6),dtype=int)
print(arr)

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
zeros_like() function
Creates an array of zeros with the same shape and type as an existing array.
syntax :
numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)
       a → Reference array (copies its shape and dtype).
       dtype (optional) → Overrides the data type.
       order (optional) → Memory layout ('C', 'F', 'A', 'K').
       shape (optional) → Allows changing the shape (new in NumPy 1.17).

'''
arr = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
                ])

arr1 = np.zeros((4,4))

arr3 = np.zeros_like(arr)
print(arr3)

# using dtype
arr3 = np.zeros_like(arr1,dtype=int) # does not copy dtype  of arr1 using its own dtype = int
print(arr3)

# using shape
arr3 = np.zeros_like(arr1,dtype=int,shape=(2,8)) # does not copy shape of arr1 using its own defined shape = 2,8
print(arr3) 

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
