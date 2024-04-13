# Cyclic sort 

is a comparison based algorithm. it is in place sorting that operates on set of values on specific range.  it sorts element by iteratively placing each element in its correct position with in the array 

## Step on How it works 

1. iteration
2. placement : for each element check if it is in the correct position. if not swap it with the element that is in its position. repeat this process until th current element is in its correct position
3. continue : move to the next element and repeat the  step two until all elements are sorted 

core concept in cyclic sort 
check , swap , move


```python


def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:  # Element is not in correct position
            correct_pos = arr[i] - 1  # Index where the element should be
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]  # Swap
        else:
            i += 1  # Move to the next element

# Example usage
arr = [3, 5, 2, 1, 4]
cyclic_sort(arr)
print("Sorted array:", arr)

```