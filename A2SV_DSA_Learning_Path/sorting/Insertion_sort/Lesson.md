## Insertion Sort

insertion sort divides the elements into two parts the sorted part and the unsorted part. 

before the first iteration only the first element belongs to the sorted part, and the sorted part extends with every iteration. 
- it looks at the first element of the unsorted element and then inserts it to the sorted part and if the element in the sorted part less then the the element in the unsorted part it swaps them this process continue until the elements in the array sorted.

we begin by assuming that a list with one item(position 0) is already sorted. one each pass, one for each item 1 through len(n) the current item is checked against those in the already sorted part, As we look back into the already sorted part, we shift those items that are greater
to the right. When we reach a smaller item or the end of the sorted part, the current item can be inserted.