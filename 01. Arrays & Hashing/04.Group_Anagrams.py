# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):

            HashMap = {}

            if len(strs) == 0:
                return [[""]]

            for word in strs:
                SortedWord = ''.join(sorted(word))

                if SortedWord not in HashMap:
                    HashMap[SortedWord] = [word]
                else:
                    HashMap[SortedWord].append(word)
            return HashMap.values()
        
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Time complexity: O(m*nlogn)
# Space complexity: O(n)