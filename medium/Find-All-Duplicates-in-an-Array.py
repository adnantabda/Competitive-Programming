# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

"""

442. Find All Duplicates in an Array
Medium
Topics
Companies

Given an integer array nums of length n where all the integers of nums are in the range 
[1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n
    Each element in nums appears once or twice.



"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
            
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates