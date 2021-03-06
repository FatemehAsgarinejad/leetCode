#Given an array of integers and an integer k, find out whether there are two distinct indices i and j
#in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = i
            else:
                if abs(dic[num] - i) <= k:
                    return True, dic[num], i, num
                else:
                    dic[num] = i
        return False
sol = Solution()
sol.containsNearbyDuplicate([1,2,3,1,2,3], 3)
