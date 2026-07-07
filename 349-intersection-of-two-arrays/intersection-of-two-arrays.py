class Solution(object):
    def intersection(self, nums1, nums2):
        common = set(nums1).intersection(set(nums2))
        return list(common)

nums1 = [1,2,3,4,5]
nums2 = [2,3]
print(Solution().intersection(nums1, nums2))      
        