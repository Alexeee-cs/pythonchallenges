def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
 
arr = [64, 71, 34, 25, 42, 17, 90, 1, 55]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])
