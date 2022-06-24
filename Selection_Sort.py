

Array = [23, 31, 45, 28, 37, 58, 28]

#trAVERSE through all array elements 
for i in range(len(Array)):
 
    #find the minimum elements in remaining 
    # unsorted array 
    min_index = i
    for j in range(i+1, len(Array)):
        print(j)
        if  Array[min_index] > Array[j]:
            min_index = j
    


    #swap the found minimum element with the first element
    Array[i], Array[min_index] = Array[min_index], Array[i]


print("Sorted array:")
for i in range(len(Array)):
    print("%d" %Array[i] , end = " "),
