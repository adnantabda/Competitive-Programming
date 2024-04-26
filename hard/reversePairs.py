# https://leetcode.com/problems/reverse-pairs/description/

"""
493. Reverse Pairs
Hard
Topics
Companies
Hint

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

    0 <= i < j < nums.length and
    nums[i] > 2 * nums[j].

 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

 

Constraints:

    1 <= nums.length <= 5 * 104
    -231 <= nums[i] <= 231 - 1



"""


class Solution:
    count = 0
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, start, mid, end):
            right_index = mid + 1
            temp = []
            for i in range(start, mid + 1):
                while right_index <= end and nums[i] > nums[right_index]:
                    temp.append(nums[right_index])
                    right_index += 1
                temp.append(nums[i])
            nums[start:start+len(temp)] = temp

        def countAndMergeSort(nums, start, end):
            if end - start <= 0:
                return 0

            mid = start + (end - start) // 2
            count = countAndMergeSort(nums, start, mid) + countAndMergeSort(nums, mid + 1, end)
            right_index = mid + 1
            for i in range(start, mid + 1):
                while right_index <= end and nums[i] > nums[right_index] * 2:
                    right_index += 1
                count += right_index - (mid + 1)
            merge(nums, start, mid, end)
            return count
        return countAndMergeSort(nums, 0, len(nums) - 1)

        