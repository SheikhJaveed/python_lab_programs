def array_operations(arr):
    def find_max_min(arr):
        return max(arr), min(arr)
    
    def second_largest(arr):
        arr = list(set(arr))
        arr.sort()
        return arr[-2] if len(arr) > 1 else None
    
    print("Max:", find_max_min(arr)[0])
    print("Min:", find_max_min(arr)[1])
    print("Second Largest:", second_largest(arr))

array_operations([1, 2, 3, 4, 5])
