
# https://leetcode.com/problems/find-the-duplicate-number/description/

"""

287. Find the Duplicate Number
Medium
Topics
Companies

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

 

Constraints:

    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.


"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):

            if nums[i] != i + 1:
                
                correct_index = nums[i] - 1 
                if nums[i] != nums[correct_index]:
                    nums[i] , nums[correct_index] = nums[correct_index] , nums[i]
                else: 
                    return nums[i]
            else:
                i +=1

        return -1