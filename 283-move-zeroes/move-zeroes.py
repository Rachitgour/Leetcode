class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        if 0 in nums:
            count += nums.count(0)
            for i in range(count):
                nums.remove(0)
                nums.append(0)
        return nums
print(Solution().moveZeroes([0, 1, 0, 3, 12]))