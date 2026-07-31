class Solution(object):
    def isAnagram(self, s, t):
        chars_01 = {}
        chars_02 = {}
        for char in s:
            chars_01[char] = chars_01.get(char, 0) + 1
        for char in t:
            chars_02[char] = chars_02.get(char, 0) + 1
        if chars_01 == chars_02:
            return True
        return False

print(Solution().isAnagram("anagram", "nagaram"))
        