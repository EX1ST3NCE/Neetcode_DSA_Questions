# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i != j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
            
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))

# Time complexity: O(n)
# Space complexity: O(1)