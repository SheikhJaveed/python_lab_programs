import numpy as np

def numpy_operations():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print("Array:")
    print(arr)
    
    print("Reverse Array:")
    print(arr[::-1])
    
    print("Principal Diagonal:")
    print(np.diagonal(arr))
    
    print("Array sorted in ascending order:")
    print(np.sort(arr, axis=None))
    
    print("Array sorted in descending order:")
    print(np.sort(arr, axis=None)[::-1])

numpy_operations()
