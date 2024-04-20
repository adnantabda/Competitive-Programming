## Bubble Sort


This sorting Algorithm makes multiple passes through a list.
It compare adjacent items and exchange those that are out of order.
each pass through a list places the next largest value in its proper place. **each item bubbles up to the location where it belongs**


if there are n items in the list then there are n-1 pairs of items that need to be compared on the first pass 

once the largest value in the list is part of a pair, it will continually be moved along until the pass is complete.

at the start of the second pass, the largest value is now in place. there are n - 1 items left to sort meaning that there will be n - 2 pairs, since each pass places the next largest value  place the total number of passes necessary will be n - 1 after completing the n - 1 passes the smallest item must be in the correct position with no further processing required. 