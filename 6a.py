def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            print(f"Found {key} at index {mid}")
            return
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    print("Key not found")

binary_search([1, 2, 3, 4, 5, 6, 7], 4)
