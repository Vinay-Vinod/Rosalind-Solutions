def binary_search(arr, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1
        
def func(arr1, arr2):
    res = []
    for val in arr2:
        answer = binary_search(arr1, 0, len(arr1)-1, val)
        if answer != -1:
            res.append(answer+1)
        else:
            res.append(answer)
        
    
    print(*res, sep=" ")

def convert(arr):
    arr = arr.split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    
    return arr

arr1 = "10 20 30 40 50"
arr2 = "40 10 35 15 40 20"

arr1 = convert(arr1)
arr2 = convert(arr2)

func(arr1, arr2)

