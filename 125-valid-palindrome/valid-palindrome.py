class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        reversed_nums = []
        for i in range(1, len(s) + 1):
            reversed_nums.append(s[-i])
        return "".join(reversed_nums) == s 
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))