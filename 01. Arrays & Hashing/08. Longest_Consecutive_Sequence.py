# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for i in numSet:
            if i - 1 not in numSet:
                c = 1
                while i + c in numSet:
                    c += 1
                longest = max(c, longest)

        return longest
    
sol = Solution()
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    
# Time complexity: O(n)
# Space complexity: O(n)