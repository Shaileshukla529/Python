import numpy as np
# array() ->the array() function is used to create an array 
# from a list, tuple, or other array-like objects.
arr = np.array([[1,2,3,4,5,6]]) # 1-d array
print(arr)
print(type(arr))
print(arr.dtype)

arr = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(arr)
print(type(arr))
print(arr.dtype)
print(arr[1,2])
print(arr.shape) # output (2,6) 1 list contain 2 list each has 6 element
print(arr.size) # tell total number of elements 12

# question create a 5X6 dimensional array
arr = np.array([
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
                ])

print(arr)
print(type(arr))
print(arr.dtype)
print(arr[1,2])
print(arr.shape) # output (5,6) 1 list contain 5 list each has 6 element
print(arr.size) # tell total number of elements 30

'''
Key Takeaways
If copy=True, a new independent array is always created.
If copy=False, NumPy avoids copying when possible (e.g., same dtype, same memory layout).
Changing dtype forces a copy, even if copy=False.
If the new array shares memory, modifying one affects the other.

'''

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# as array syntax
# numpy.asarray(a, dtype=None, order=None)

lst = [1, 2, 3]
arr = np.asarray(lst)

# using asarray() with a list (creates a new NumPy array)
print(arr)  # Output: [1 2 3]
print(type(arr))  # <class 'numpy.ndarray'>

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Using asarray() with an existing NumPy array (no copy)

arr1 = np.array([10, 20, 30])  # Original array
arr2 = np.asarray(arr1)  # No new copy is made

arr1[0] = 99  # Modify original array
print(arr2)  # Output: [99 20 30] (same memory reference!)

# Since arr1 is already a NumPy array, asarray() 
# does not create a new copy—modifications affect both.

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ✅ When dtype is different, asarray() creates a new copy.
arr1 = np.array([1, 2, 3])
arr2 = np.asarray(arr1, dtype=float)  # Forces a new copy due to dtype change

arr1[0] = 99  # Modify original array
print(arr2)  # Output: [1. 2. 3.] (unchanged)

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Using order parameter
# ✅ Memory layout can be controlled using order.

arr_c = np.asarray([[1, 2], [3, 4]], order='C')  # Row-major (default)
arr_f = np.asarray([[1, 2], [3, 4]], order='F')  # Column-major

print(arr_c.flags['C_CONTIGUOUS'])  # True
print(arr_f.flags['F_CONTIGUOUS'])  # True

''' 
When to Use np.asarray()
Use asarray() when working with functions that expect NumPy arrays
but you don’t want unnecessary copies.
Use array() if you always want a new copy, even if the input is already an array.

'''
