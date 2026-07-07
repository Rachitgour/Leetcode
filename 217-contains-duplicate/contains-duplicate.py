class Solution(object):
    def containsDuplicate(self, nums):
        arr = set()
        for num in nums:
            if num in arr:
                return True
            arr.add(num)
        return False
print(Solution().containsDuplicate([2,14,18,22,22]))