class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        r1 = 0
        r2 = 1
        
        while (r2 < len(nums)):
            print("Before LOOP: First pointer: ", r1, " Second Pointer: ", r2)
            if nums[r1] != 0 and nums[r2] == 0:
                # set r1 = r2 and only increase r2
                r1 = r2
                r2 += 1
                
            elif nums[r1] == 0 and nums[r2] != 0:
                # do something
                temp = nums[r2]
                nums[r1] = temp
                nums[r2] = 0
                r1 += 1
                r2 += 1
            elif nums[r1] != 0 and nums[r2] != 0:
                r1 += 1
                r2 += 1
            elif nums[r1] == 0 and nums[r2] == 0:
                r2 += 1
            print("AFTER LOOP: First pointer: ", r1, " Second Pointer: ", r2)
        return nums
                
                