class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        left = str(left)
        right = str(right)
        for char in left:
            if char == "0" : 
                break
            else:
                int(char) % int(char) == 0
                
