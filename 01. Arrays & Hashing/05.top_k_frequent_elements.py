# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums, k):
        ans = []
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        print(hashmap)
        for key, value in sorted(hashmap.items(), key=lambda x:x[1], reverse=True):
            ans.append(key)
        return ans[:k]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
    
# Time complexity: O(nlogn)
# Space complexity: O(n)