def search(arr: list, target) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


print(search(arr=[1, 2, 3, 4, 5, 6], target=6))
