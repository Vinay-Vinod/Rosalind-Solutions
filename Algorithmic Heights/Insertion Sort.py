def insertionSort(arr):
    swap = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                swap += 1
        arr[j+1] = key
        
    return swap

def main(arr):
    arr = list(map(int, arr.split()))
    x = insertionSort(arr)
    print(x)
    

arr = "6 10 4 5 1 2"
main(arr)
