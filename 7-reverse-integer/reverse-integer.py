class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        arr = int(str(x)[::-1])
        arr = arr * sign

        if arr < -2**31 or arr > 2**31 - 1:
            return 0

        return arr


print(Solution().reverse(-123))
