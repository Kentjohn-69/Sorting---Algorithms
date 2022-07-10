
def insertSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        

        # move elements of arr[0..i-1], that are 
        #greater than key, to one position ahead
        #of thier current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

arr = [12, 34, 65, 78,94 ,46, 92, 16]

insertSort(arr)
for i in range(len(arr)):
    print("%d" %arr[i] , end = " ")