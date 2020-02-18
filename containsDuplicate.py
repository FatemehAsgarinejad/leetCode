#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array,
#and it should return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1
        return False

sol = Solution()
sol.containsDuplicate([1,2,3,1])
