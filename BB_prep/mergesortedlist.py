class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        '''w = len(nums1) - 1
        r1 = m - 1
        r2 = n - 1
        
        while (r2 >= 0) and (r1 >= 0):
            maxNum = max(nums1[r1], nums2[r2])
            
            if maxNum == nums1[r1]:
                nums1[w] = nums1[r1]
                r1 -= 1
                w -= 1
            else:
                nums1[w] = nums2[r2]
                r2 -= 1
                w -= 1
        return nums1'''
        p1 = m - 1
        p2 = n - 1

        # And move p backward through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        return nums1