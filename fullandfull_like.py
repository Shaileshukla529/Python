import numpy as np
'''
numpy.full()
Creates a new array filled with a specified constant value.

syntax: numpy.full(shape, fill_value, dtype=None, order='C')
         shape → Tuple defining the shape of the array (e.g., (rows, cols)).
         fill_value → The constant value to fill the array with.
         dtype (optional) → Data type of the array (default: inferred from fill_value).
         order (optional) → Memory layout ('C' for row-major, 'F' for column-major).
✅ Unlike np.zeros() or np.ones(), this allows you to specify any fill value

'''

arr = np.full((3,5),16)
print(arr)

arr = np.full(4,16)
print(arr)

arr = np.full((0,6),16)
print(arr)

'''
numpy.full_like()
Creates a new array with the same shape and type as an existing array, filled with a specified value.

syntax: numpy.full_like(a, fill_value, dtype=None, order='K', subok=True, shape=None)
          a → Reference array (copies its shape and dtype).
          fill_value → The constant value to fill the new array.
          dtype (optional) → Overrides the data type.
          order (optional) → Memory layout ('C', 'F', 'A', 'K').
          shape (optional) → Allows changing the shape (new in NumPy 1.17).

  Faster than np.full() if you already have an array whose shape and type you want to use.          

'''

arr = np.array([[1, 2, 3], [4, 5, 6]])
full_arr = np.full_like(arr, 9)  # Same shape as arr, filled with 9

print(full_arr)
