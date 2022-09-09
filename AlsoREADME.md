More types of Sorting algorithm

6. HeapSort

Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.

*Heap sort is an in-place algorithm. 
*Its typical implementation is not stable, but can be made *stable (See this)
*Typically 2-3 times slower than well-implemented QuickSort.  *The reason for slowness is a lack of locality of reference.

Advantages of heapsort:
*Efficiency* –  The time required to perform Heap sort increases logarithmically while other algorithms may grow exponentially slower as the number of items to sort increases. This sorting algorithm is very efficient.
*Memory Usage* – Memory usage is minimal because apart from what is necessary to hold the initial list of items to be sorted, it needs no additional memory space to work
*Simplicity* –  It is simpler to understand than other equally efficient sorting algorithms because it does not use advanced computer science concepts such as recursion.

$Algorithm for Heapify:
heapify(array)
 Root = array[0]

Largest = largest( array[0] , array [2 * 0 + 1]/ array[2 * 0 + 2])
if(Root != Largest)
 Swap(Root, Largest)

$How does Heapify work? 

 
Array = {1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17}
Corresponding Complete Binary Tree is:

                 1
              /     \
           3         5
        /    \     /  \
      4      6   13  10
     / \    / \
   9   8  15 17

The task to build a Max-Heap from above array.

Total Nodes = 11.
Last Non-leaf node index = (11/2) – 1 = 4.
Therefore, last non-leaf node = 6.

To build the heap, heapify only the nodes: [1, 3, 5, 4, 6] in reverse order.

Heapify 6: Swap 6 and 17.

                 1
              /     \
           3         5
        /    \      /  \
     4      17   13  10
    / \    /  \
  9   8  15   6

Heapify 4: Swap 4 and 9.

                 1
              /     \
           3         5
        /    \      /  \
     9      17   13  10
    / \    /  \
  4   8  15   6

Heapify 5: Swap 13 and 5.

                 1
              /     \
           3         13
        /    \      /  \
     9      17   5   10
    / \    /  \
 4   8  15   6

Heapify 3: First Swap 3 and 17, again swap 3 and 15.

                 1
             /     \
        17         13
       /    \      /  \
    9      15   5   10
   / \    /  \
 4   8  3   6

Heapify 1: First Swap 1 and 17, again swap 1 and 15, finally swap 1 and 6.

                 17
              /      \
          15         13
         /    \      /  \
       9      6    5   10
      / \    /  \
    4   8  3    1

7. CountingSort

Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then do some arithmetic to calculate the position of each object in the output sequence. 

Characteristics of counting sort:
*Counting sort makes assumptions about the data, for example, it assumes that values are going to be in the range of 0 to 10 or 10 – 99 etc, Some other assumptions counting sort makes are input data will be all real numbers.
*Like other algorithms this sorting algorithm is not a comparison-based algorithm, it hashes the value in a temporary count array and uses them for sorting.
*It uses a temporary array making it a non In Place algorithm.

Let us understand it with the help of an example.

For simplicity, consider the data in the range 0 to 9. 
Input data: {1, 4, 1, 2, 7, 5, 2}
Take a count array to store the count of each unique object.
Now, store the count of each unique element in the count array
If any element repeats itself, simply increase its count.
Here, the count of each unique element in the count array is as shown below:
Index:     0  1  2  3  4  5  6  7  8  9
Count:    0  2  2  0   1  1  0  1  0  0
Modify the count array such that each element at each index stores the sum of previous counts.
Index:      0  1  2  3  4  5  6  7  8  9
Count:     0  2  4  4  5  6  6  7  7  7
The modified count array indicates the position of each object in the output sequence.
Find the index of each element of the original array in the count array. This gives the cumulative count.
Rotate the array clockwise for one time.
Index:     0 1 2 3 4 5 6 7 8 9 
Count:     0 0 2 4 4 5 6 6 7 7
 Output each object from the input sequence followed by increasing its count by 1.
Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 0.
Put data 1 at index 0 in output. Increase count by 1 to place next data 1 at an index 1 greater than this index.
After placing each element at its correct position, decrease its count by one.

8. RadixSort

The lower bound for the Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(nLogn), i.e., they cannot do better than nLogn. Counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in the range from 1 to k.

What if the elements are in the range from 1 to n2? 

We can’t use counting sort because counting sort will take O(n2) which is worse than comparison-based sorting algorithms. Can we sort such an array in linear time? 

Radix Sort is the answer. The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort. 

The Radix Sort Algorithm 

Do the following for each digit I where I varies from the least significant digit to the most significant digit. Here we will be sorting the input array using counting sort (or any stable sort) according to the i’th digit.

Example:

Original, unsorted list: 170, 45, 75, 90, 802, 24, 2, 66 Sorting by least significant digit (1s place) gives: [*Notice that we keep 802 before 2, because 802 occurred before 2 in the original list, and similarly for pairs 170 & 90 and 45 & 75.] 170, 90, 802, 2, 24, 45, 75, 66 Sorting by next digit (10s place) gives: [*Notice that 802 again comes before 2 as 802 comes before 2 in the previous list.] 802, 2, 24, 45, 66, 170, 75, 90 Sorting by the most significant digit (100s place) gives: 2, 24, 45, 66, 75, 90, 170, 802

%What is the running time of Radix Sort?

Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for the decimal system, b is 10. What is the value of d? If k is the maximum possible value, then d would be O(logb(k)). So overall time complexity is O((n+b) * logb(k)). Which looks more than the time complexity of comparison-based sorting algorithms for a large k. Let us first limit k. Let k <= nc where c is a constant. In that case, the complexity becomes O(nLogb(n)). But it still doesn’t beat comparison-based sorting algorithms. 
What if we make the value of b larger? What should be the value of b to make the time complexity linear? If we set b as n, we get the time complexity as O(n). In other words, we can sort an array of integers with a range from 1 to nc if the numbers are represented in base n (or every digit takes log2(n) bits). 

Applications of Radix Sort: 

*In a typical computer, which is a sequential random-access machine, where the records are keyed by multiple fields radix sort is used. For eg., you want to sort on three keys month, day and year. You could compare two records on year, then on a tie on month and finally on the date. Alternatively, sorting the data three times using Radix sort first on the date, then on month, and finally on year could be used.
*It was used in card sorting machines with 80 columns, and in each column, the machine could punch a hole only in 12 places. The sorter was then programmed to sort the cards, depending upon which place the card had been punched. This was then used by the operator to collect the cards which had the 1st row punched, followed by the 2nd row, and so on.

Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort? 

If we have log2n bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide range of input numbers. The constant factors hidden in asymptotic notation are higher for Radix Sort and Quick-Sort uses hardware caches more effectively. Also, Radix sort uses counting sort as a subroutine and counting sort takes extra space to sort numbers.

Key points about Radix Sort:

Some key points about radix sort are given here

1.It makes assumptions about the data like the data must be between a range of elements.
2.Input array must have the elements with the same radix and width.
3.Radix sort works on sorting based on an individual digit or letter position.
4.We must start sorting from the rightmost position and use a stable algorithm at each position.
5.Radix sort is not an in-place algorithm as it uses a temporary count array.

9. BucketSort

Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider the following problem. 
Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range. How do we sort the numbers efficiently?
A simple way is to apply a comparison based sorting algorithm. The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(n Log n), i.e., they cannot do better than nLogn. 
Can we sort the array in linear time? Counting sort can not be applied here as we use keys as index in counting sort. Here keys are floating point numbers.  

Time Complexity: If we assume that insertion in a bucket takes O(1) time then steps 1 and 2 of the above algorithm clearly take O(n) time. The O(1) is easily possible if we use a linked list to represent a bucket (In the following code, C++ vector is used for simplicity). Step 4 also takes O(n) time as there will be n items in all buckets. 
The main step to analyze is step 3. This step also takes O(n) time on average if all numbers are uniformly distributed (please refer CLRS book for more details)