def binary_search(arr, targe, high, low):
    mid = (high + low) // 2
    if low > high:
        return False
    elif arr[mid] == targe:
        return True
    elif arr[mid] > targe:
        return binary_search(arr, targe, mid - 1, low)
    elif arr[mid] < targe:
        return binary_search(arr, targe, high, mid + 1)

arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr, 1, len(arr) - 1, 0))