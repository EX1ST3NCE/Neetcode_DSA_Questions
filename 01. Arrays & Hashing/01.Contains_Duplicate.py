#  https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        unique_nums = set(nums)
        
        if len(nums) == len(unique_nums):
            return False
        else:
            return True

sol = Solution()
print(sol.containsDuplicate([1,2,3,4,5]))

# Time_complexity - 0(n)
# Space_complexity - 0(n)