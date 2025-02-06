import numpy as np

'''
numpy.identity() Function
The numpy.identity() function creates an identity matrix, which is a square matrix with ones (1s) on the main diagonal and zeros (0s) elsewhere.
It is similar to numpy.eye(), but only creates square matrices (i.e., N x N).

 syntax : numpy.identity(n, dtype=None)
            n → Number of rows and columns (creates an n x n identity matrix).
            dtype (optional) → Specifies the data type of the array (default: float).

'''
# Basic Identity Matrix (N x N)
arr = np.identity(3)
print(arr)

# Integer Identity Matrix (dtype=int)
arr = np.identity(4, dtype=int)
print(arr)

'''
Key Differences:                           np.identity()                                           np.eye()
Feature                                   np.identity(n)	                                    np.eye(N, M, k)
Creates Square Matrices Only	       ✅ Yes (N x N only)	                                   ❌ No (N x M possible)
Allows Custom Number of Columns             	❌ No	                                           ✅ Yes
Allows Diagonal Offset (k Parameter)	        ❌ No	                                           ✅ Yes
Default Data Type	                            float	                                             float     


'''
