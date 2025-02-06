import numpy as np

'''
Basic Random Number Generation

  np.random.rand() → Uniformly distributed random numbers (0 to 1)
  Generates random numbers between 0 and 1 (continuous uniform distribution).

'''

arr = np.random.rand(3, 2)  # 3 rows, 2 columns
print(arr)

'''
np.random.randint() → Random integers
Generates random integers between a given range.

'''
arr = np.random.randint(10, 50, size=(3, 2))  # Random ints from 10 to 49
print(arr)

'''
np.random.randn() → Normally distributed random numbers
Generates numbers from a standard normal distribution (mean = 0, std = 1).

🔹 Output (values vary, can be negative or positive):
'''

arr = np.random.randn(3, 2)
print(arr)

'''
Random Choice & Shuffle
np.random.choice() → Selects random elements from an array
🔹 Output (random sample from arr):
'''
arr = np.array([10, 20, 30, 40, 50])
choice = np.random.choice(arr, size=3)  # Pick 3 random elements
print(choice)


'''
np.random.shuffle() → Shuffles an array in place
🔹 Output (shuffled values):
'''

arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

'''
Seeding Randomness (np.random.seed())
To get reproducible random numbers, set a seed:
🔹 Output (always the same for seed 42):
'''
np.random.seed(42)
print(np.random.rand(3))  # Same output every time!

'''
Other Random Distributions
np.random.uniform() → Random numbers from a uniform distribution
Generates random numbers between low and high, where each number is equally likely
'''
arr = np.random.uniform(5, 10, size=(2, 3) )  # Between 5 and 10
print(arr)

'''
np.random.normal() → Random numbers from a normal distribution
Generates numbers centered around mean with a given standard deviation (std).
'''
arr = np.random.normal(loc=50, scale=10, size=(3, 3))  # Mean=50, Std=10
print(arr)