## Counting Sort

Counting sort is a non-comparison based sorting algorithm that operates by counting the occurrences of each unique element in the input array. It assumes that the input consists of integers within a specific range. Counting sort works efficiently when the range of input elements is not significantly greater than the number of elements to be sorted.

Here's a step-by-step explanation of how counting sort works:

1. **Counting Occurrences**: First, determine the range of input values (minimum and maximum) to establish the size of the counting array. Create a counting array (also called a frequency array) of size equal to the range plus one (to account for zero-based indexing), initialized with zeros. Each index of the counting array represents a unique value within the range.

2. **Counting Frequencies**: Iterate through the input array, and for each element, increment the corresponding index in the counting array. This step counts the frequency of each unique element in the input array.

3. **Cumulative Sum**: Modify the counting array to contain the cumulative sum of counts. This cumulative sum represents the position of each element in the sorted output array.

4. **Build the Sorted Array**: Iterate through the original input array again. For each element, find its position in the counting array. Decrement the count in the counting array for that element. Use this count as the index to place the element in the correct position in the sorted array.

5. **Output the Sorted Array**: The sorted array is obtained after placing each element in its correct position using the counting array.

Let's implement counting sort in Python:

```python
def counting_sort(arr):
    # Find the range of input values
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1
    
    # Initialize the counting array with zeros
    count_arr = [0] * range_of_elements
    
    # Count occurrences of each element
    for num in arr:
        count_arr[num - min_val] += 1
    
    # Modify counting array to store cumulative sum
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    # Build the sorted array
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1
    
    return sorted_arr

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
```

This implementation of counting sort has a time complexity of O(n + k), where n is the number of elements in the input array and k is the range of the input. However, it requires extra space for the counting array, making it less efficient for large ranges of input values.