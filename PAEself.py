class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefix, postfix, arr = [None] * length, [None] * length,  [None] * length
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        print("Prefix: ", prefix)

        postfix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        print("postifx", postfix)

        arr[0] = postfix[1]
        arr[len(arr) - 1] = prefix[len(arr) - 2]
        for i in range(1, len(arr) - 1):
            arr[i] = prefix[i - 1] * postfix[i + 1]
        return arr
        
        

        