import numpy as np

'''
The np.eye() function creates an identity matrix, 
which is a square matrix with ones (1s) on the main diagonal and zeros (0s) elsewhere.

syntax : numpy.eye(N, M=None, k=0, dtype=None, order='C')
           N → Number of rows in the output matrix.
           M (optional) → Number of columns (default is N, making a square matrix).
           k (optional) → Diagonal offset:
           k=0 → Main diagonal (default).
           k>0 → Moves diagonal above the main one.
           k<0 → Moves diagonal below the main one.
           dtype (optional) → Data type of the array (default: float).
           order (optional) → Memory layout ('C' for row-major, 'F' for column-major).


'''
# Basic Identity Matrix (N x N)
arr = np.eye(3)
print(arr)

# Rectangular Identity Matrix (N x M)
arr = np.eye(3, 5)  # 3 rows, 5 columns
print(arr)

# Moving the Diagonal (k Parameter)
# ✅ Diagonal is shifted up by one row.
arr = np.eye(4, 4, k=1)  # Shift diagonal 1 step up
print(arr)

# ✅ Diagonal is shifted down by one row.
arr = np.eye(4, 4, k=-1)  # Shift diagonal 1 step down
print(arr)

# Specifying dtype
#✅ Integer elements instead of floats.
arr = np.eye(3, dtype=int)  # Integer identity matrix
print(arr)
