def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        while arr[j] < arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

arr = [2, 7, 5, 3, 4, 1]
insertion_sort(arr)
print(arr)
# 0, 1, 2, 3, 4, 5
