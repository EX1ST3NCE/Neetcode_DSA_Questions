# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}

        for letter in s:
            if letter in dictionary:
                 dictionary[letter] += 1
            else:
                dictionary[letter] = 1

        for letter in t:
            if letter in dictionary:
                 dictionary[letter] -= 1
            else:
                return False

        for val in dictionary.values():
            if val != 0:
                return False
        return True
    
sol = Solution()
print(sol.isAnagram('anagram', 'nagaram'))

# Time_complexity - 0(n)
# Space_complexity - 0(n)