class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums == None) or (len(nums)==0):
            return 0
        if (len(nums) == 1):
            return nums[0]
        mv = nums[0]
        cv = nums[0] #1
        sv = nums[0] #1
        for i in nums[1:]:
            if i > sv + i:
                mv = i
                sv = i
            elif sv + i > mv:
                mv = sv + i
                sv = sv + i
            else:
                sv = sv + i
            if cv < mv:
                cv = mv
        return cv

s=Solution()

input_data = [-2,1,-3,4,-1,2,1,-5,4] #maxSubArray
print(s.maxSubArray(input_data))