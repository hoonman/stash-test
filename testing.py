def binary_search(arr, t, high, low):
    mid = (high + low) // 2
    if low > high:
        return False
    elif arr[mid] == t:
        return True
    elif arr[mid] > t:
        return binary_search(arr, t, mid - 1, low)
    elif arr[mid] < t:
        return binary_search(arr, t, high, mid + 1)

arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr, 1, len(arr) - 1, 0))