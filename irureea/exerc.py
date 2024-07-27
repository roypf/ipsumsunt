import cupy as cp
import numpy as np

# Create a CuPy array
cupy_array = cp.array([1, 2, 3, 4, 5])

# Convert CuPy array to NumPy array
numpy_array = cp.asnumpy(cupy_array)

# Now you can work with the NumPy array
print(numpy_array)
