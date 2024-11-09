def interchange(arr):
    if arr[0] != arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]

arr = [22 ,1 , 3, 4, 5 , 32, 66, 82, 2]
print(f"uninsterchanged array: {arr}")
interchange(arr)
print(f"interchanged array: {arr}")