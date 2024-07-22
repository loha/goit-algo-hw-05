def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return iterations, arr[mid]

    if left < len(arr):
        upper_bound = arr[left]
    else:
        upper_bound = None

    return iterations, upper_bound

# Приклад використання:
sorted_array = [0.1, 0.5, 1.3, 2.7, 3.6, 4.0, 5.8]
target_value = 2.0
result = binary_search(sorted_array, target_value)
print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")
