import numpy as np
'''
The np.arange() function is used to create evenly spaced values within a given range. 
It works similarly to Python's
built-in range() but returns a NumPy array instead of a list.

SYntax of arrange
np.arange(start, stop, step, dtype=None)
# Default start=0, step=1
'''
# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

arr = np.arange(11) # here 11 is stop value
print(arr)

arr = np.arange(1, 100, 5, dtype=None)
print(arr)

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Specifying dtype

arr = np.arange(1, 5, dtype=float)
print(arr)

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

arr = np.arange(10, 1, -2)  # Count backward from 10 to 2
print(arr)

# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
Difference Between np.arange() and np.linspace()
Feature	                    np.arange()                      	    np.linspace()
Step-based	          Defines values using step	       Defines values using num (number of points)
Excludes Stop       	          Yes	                         No (includes stop by default)
Works with Float Steps? 	May cause precision issues	 Works better for precise spacing


'''
# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


