

def bubbleSort(arr):
    n = len(arr)
    #traverse through all array elements
    for i in range(n):
       
        #last i element are already in place 
        for j in range(0 , n-i-1):
           
            
            #traverse the array from 0 to n-i-1
            #swap if the element is greater 
            #than the next element
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    

arr = [12,45,67,54,32,72,17]

bubbleSort(arr)

print("The sorted array:")
for i in range(len(arr)):
    print("%d" %arr[i], end  = " ")
            
