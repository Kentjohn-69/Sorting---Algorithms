# Sorting - Algorithms
 Just example of sorting

 This is me trying to learn a sorting algorithm that focus in a array.

1. BubbleSort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong   order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

Input: arr[] = {5, 1, 4, 2, 8}

First Pass: 

Bubble sort starts with very first two elements, comparing them to check which one is greater.
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4 
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2 
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass: 

Now, during second iteration it should look like this:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ) 
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 ) 
Third Pass: 

Now, the array is already sorted, but our algorithm does not know if it is completed.
The algorithm needs one whole pass without any swap to know it is sorted.
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 

2. InsertionSort
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

Consider an example: arr[]: {12, 11, 13, 5, 6}

   12, 11, 13, 5, 6   
First Pass:

Initially, the first two elements of the array are compared in insertion sort.
   12, 11, 13, 5, 6   
Here, 12 is greater than 11 hence they are not in the ascending order and 12 is not at its correct position. Thus, swap 11 and 12.
So, for now 11 is stored in a sorted sub-array.
   11, 12, 13, 5, 6   
Second Pass:

Now, move to the next two elements and compare them
   11, 12, 13, 5, 6   
Here, 13 is greater than 12, thus both elements seems to be in ascending order, hence, no swapping will occur. 12 also stored in a sorted sub-array along with 11
Third Pass:

Now, two elements are present in the sorted sub-array which are 11 and 12
Moving forward to the next two elements which are 13 and 5
   11, 12, 13, 5, 6   
Both 5 and 13 are not present at their correct place so swap them
   11, 12, 5 , 13, 6   
After swapping, elements 12 and 5 are not sorted, thus swap again
   11, 5, 12, 13, 6   
Here, again 11 and 5 are not sorted, hence swap again
   5, 11, 12, 13, 6   
here, it is at its correct position
Fourth Pass:
Now, the elements which are present in the sorted sub-array are 5, 11 and 12
Moving to the next two elements 13 and 6
   5, 11, 12, 13, 6   
Clearly, they are not sorted, thus perform swap between both
   5, 11, 12, 6, 13   
Now, 6 is smaller than 12, hence, swap again
   5, 11, 6, 12, 13   
Here, also swapping makes 11 and 6 unsorted hence, swap again
   5, 6, 11, 12, 13   
Finally, the array is completely sorted.

3. SelectionSort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from the unsorted part and putting it at the beginning. 

The algorithm maintains two subarrays in a given array.

The subarray which already sorted. 
The remaining subarray was unsorted.
In every iteration of the selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 

Lets consider the following array as an example: arr[] = {64, 25, 12, 22, 11}

First pass:
For the first position in the sorted array, the whole array is traversed from index 0 to 4 sequentially. The first position where 64 is stored presently, after traversing whole array it is clear that 11 is the lowest value.
   64, 25, 12, 22, 11   
Thus, replace 64 with 11. After one iteration 11, which happens to be the least value in the array, tends to appear in the first position of the sorted list.
   11, 25, 12, 22, 64   
Second Pass:

For the second position, where 25 is present, again traverse the rest of the array in a sequential manner.
   11, 25, 12, 22, 64   
After traversing, we found that 12 is the second lowest value in the array and it should appear at the second place in the array, thus swap these values.
   11, 12, 25, 22, 64   
Third Pass:

Now, for third place, where 25 is present again traverse the rest of the array and find the third least value present in the array.
   11, 12, 25, 22, 64   
While traversing, 22 came out to be the third least value and it should appear at the third place in the array, thus swap 22 with element present at third position.
   11, 12, 22, 25, 64   
Fourth pass:

Similarly, for fourth position traverse the rest of the array and find the fourth least element in the array 
As 25 is the 4th lowest value hence, it will place at the fourth position.
   11, 12 , 22, 25, 64   
Fifth Pass:

At last the largest value present in the array automatically get placed at the last position in the array
The resulted array is the sorted array.
   11, 12, 22, 25, 64.

4. MergeSort   

The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm. In this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner.

Merge Sort Working Process:
Think of it as a recursive algorithm continuously splits the array in half until it cannot be further divided. This means that if the array becomes empty or has only one element left, the dividing will stop, i.e. it is the base case to stop the recursion. If the array has multiple elements, split the array into halves and recursively invoke the merge sort on each of the halves. Finally, when both halves are sorted, the merge operation is applied. Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.

Algorithm:
step 1: start

step 2: declare array and left, right, mid variable

step 3: perform merge function.
    if left > right
        return
    mid= (left+right)/2
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    merge(array, left, mid, right)

step 4: Stop

5. QuickSort

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

*Always pick the first element as a pivot.
*Always pick the last element as a pivot (implemented below)
*Pick a random element as a pivot.
*Pick median as the pivot.

The key process in quickSort is a partition(). The target of partitions is, given an array and an element x of an array as the pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

$Pseudo Code for recursive QuickSort function:

/* low  –> Starting index,  high  –> Ending index */

quickSort(arr[], low, high) {

    if (low < high) {

        /* pi is partitioning index, arr[pi] is now at right place */

        pi = partition(arr, low, high);

        quickSort(arr, low, pi – 1);  // Before pi

        quickSort(arr, pi + 1, high); // After pi

    }

}
$Pseudo code for partition()  

/* This function takes last element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot */

partition (arr[], low, high)

{

    // pivot (Element to be placed at right position)
pivot = arr[high];  

 i = (low – 1)  // Index of smaller element and indicates the 
// right position of pivot found so far

for (j = low; j <= high- 1; j++){

 // If current element is smaller than the pivot
if (arr[j] < pivot){
i++;    // increment index of smaller element
 swap arr[i] and arr[j]
     }
 }

    swap arr[i + 1] and arr[high])
return (i + 1)
}