def BubbleSort(arr = []):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[j + 1]:
    
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [21, 32, 22, 12, 1, 3, 54, 35, 19 , 18, 99]
print(f"unsorted list: {arr}")
BubbleSort(arr)
print(f"sorted list: {arr}")