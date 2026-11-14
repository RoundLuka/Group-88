# def recursive_reverse(string):
#     if len(string) == 0:
#         return ""
#     return recursive_reverse(string[1:]) + string[0]

# print(recursive_reverse("Luka"))

# O(nlogn)
# n = 6

# O(n^2)
# O(2n)
# for i in range(n):
# for j in range(n):


# best case o(n)
# worst case (n^2)
# avrg(n^2)

# def insertion_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] < arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp

# arr = [5, 6, 3, 1, 7, 5, 3, 9]
# insertion_sort(arr)
# print(arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0 # left
        j = 0 # right
        k = 0 # main

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1    


arr = [4, 12, 6, 235, 23,6, 9, 215, 14]

merge_sort(arr)
print(arr)

[].sort()