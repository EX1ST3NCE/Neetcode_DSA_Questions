# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        HashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[n] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))

# Time_complexity - 0(n)
# Space_complexity - 0(n)