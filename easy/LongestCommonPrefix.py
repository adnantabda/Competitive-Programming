"""

14. Longest Common Prefix
Easy
Topics
Companies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""

def commonStr(strs):

    common = ""
    prev_length = 0
    for i in range(0 , len(strs)):
        for j in range(0 , len(strs[i])):
            if i < len(strs) and j < len(strs[i + 1]):
                print(strs[i])
                print(strs[i][j])
                print("the length " , len(strs[i + 1]))
                print("compared with " + strs[i + 1][j])
                print([i , j])
                if strs[i][j] == strs[i + 1][j] and j < len(strs[i- 1]):
                    common = common + common.join(strs[i][j])
                    prev_length = prev_length + 1
    
    return common

 
    

print(commonStr( ["flower","flow","flight"]))
print("-----------")
print(commonStr(["dog","racecar","car"]))