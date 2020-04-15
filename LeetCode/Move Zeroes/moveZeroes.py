class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        slow = 0
        fast = 0
        while fast < len(nums):
            if not nums[fast] == 0:
                if nums[slow] == 0:
                    tmp = nums[slow]
                    nums[slow] = nums[fast]
                    nums[fast] = tmp
                slow = slow + 1
            fast = fast  + 1

s=Solution()

input_data = [0,1,0,3,12] #moveZeroes
s.moveZeroes(input_data)
print(input_data)