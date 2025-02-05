import numpy as np

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
Both functions create arrays without initializing the values, meaning the contents could be random garbage values from memory.
They are useful when you want to allocate space quickly without setting initial values.

empty() function
Creates a new uninitialized array with a specified shape and data type.

syntax : numpy.empty(shape, dtype=None, order='C')
   shape → Tuple specifying the shape of the array (e.g., (rows, cols)).
   dtype (optional) → Specifies the data type (int, float, etc.). Default is float.
   order (optional) → Memory layout ('C' for row-major, 'F' for column-major).

   🔹 Output (values are uninitialized, random garbage from memory):
   ✅ Faster than np.zeros() because it doesn’t initialize values.

'''
arr = np.empty(5)
print(arr)

arr = np.empty((2,3))
print(arr)

arr = np.empty((1,2),dtype=int)
print(arr)

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
empty_like() function
Creates a new uninitialized array with the same shape and data type as an existing array.
syntax :
numpy.empty_like(a, dtype=None, order='K', subok=True, shape=None)
       a → Reference array (copies its shape and dtype).
       dtype (optional) → Overrides the data type.
       order (optional) → Memory layout ('C', 'F', 'A', 'K').
       shape (optional) → Allows changing the shape (new in NumPy 1.17).

       ✅ Faster than np.empty_like() since values are not initialized.

'''
arr = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
                ])

arr1 = np.empty((1,4))

arr3 = np.empty_like(arr)
print(arr3)

# using dtype
arr3 = np.empty_like(arr1,dtype=int) # does not copy dtype  of arr1 using its own dtype = int
print(arr3)

# using shape
arr3 = np.empty_like(arr1,dtype=int,shape=(2,2)) # does not copy shape of arr1 using its own defined shape = 2,8
print(arr3) 

#  changing the value using indexing
arr3[:] = 10
print(arr3)

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
