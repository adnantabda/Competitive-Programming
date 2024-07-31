def next_(nums1, nums2):
    hash_ = {}
    result = [-1 for i in nums1]

    for i in nums1:
        hash_[i] = nums1.index(i)

    for i in range(len(nums2)):
        if nums2[i] in hash_:
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    result[hash_[nums2[i]]] = nums2[j]
                    break

    return result


"""
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.


Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


"""

print(next_([2, 4], [1, 2, 3, 4]))