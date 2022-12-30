# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        left_product[0] = 1
        right_product[0] = 1

        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
            right_product[len(nums) - 1 - i] = right_product[len(nums) - i] * nums[len(nums) - i]

        res = []

        for i in range(len(nums)):
            res.append(left_product[i] * right_product[i])
        return res

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))

# Time complexity: O(n)
# Space complexity: O(n)