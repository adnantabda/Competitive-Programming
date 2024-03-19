
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

"""

448. Find All Numbers Disappeared in an Array
Easy

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        i = 0 
        while i  < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i] , nums[correct_index] = nums[correct_index] , nums[i]
            else : 
                i +=1 
        

        missing_numbers = []

        for i in range(0 , len(nums)): 
            if nums[i] != i + 1 : 
                missing_numbers.append(i + 1)

        return missing_numbers
    

# Adnan Tahir