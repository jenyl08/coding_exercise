class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        set에 없으면 추가하고, 있으면 삭제하게 만들면, 마지막에 남는건 홀수로 있는거
        """
        set_nums = set([])
        for i in nums:
            if i in set_nums:
                set_nums.remove(i)
            else:
                set_nums.add(i)
        for i in set_nums:
            return i

s=Solution()

input_data = [1,4,2,1,2] #singleNumber
print(s.singleNumber(input_data))