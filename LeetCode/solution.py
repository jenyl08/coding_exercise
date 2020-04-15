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
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def hn(n):
            sum = 0
            while n >= 10:
                s = n % 10
                sum = sum + s * s
                n = int(n / 10)
            sum = sum + n * n
            return sum

        set_nums = set([])

        while True:
            if n == 1:
                return True
            else:
                n = hn(n)
                if n in set_nums:
                    return False
                else:
                    set_nums.add(n)
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
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == None:
            return 0

        if len(prices) < 2:
            return 0

        profit = 0
        for i in range(len(prices[1:])):
            if prices[i + 1] > prices[i]:
                profit = profit + prices[i + 1] - prices[i]
        return profit
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        return_list = []
        dic_anas = {}
        for strc in strs:
            strc_s = "".join(sorted(strc))
            if strc_s in dic_anas:
                dic_anas[strc_s].append(strc)
            else:
                dic_anas[strc_s] = [strc]
        for list_str in dic_anas:
            return_list.append(dic_anas[list_str])

        return return_list
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        return_count = 0
        set_arr = set(arr)

        for i in arr:

            j = int(i + 1)
            if j in set_arr:
                return_count = return_count + 1

        return return_count

s=Solution()

input_data = [1,4,2,1,2] #singleNumber
print(s.singleNumber(input_data))

input_data = 19 #isHappy
print(s.isHappy(input_data))

input_data = [-2,1,-3,4,-1,2,1,-5,4] #maxSubArray
print(s.maxSubArray(input_data))

input_data = [0,1,0,3,12] #moveZeroes
s.moveZeroes(input_data)
print(input_data)

input_data = [7,1,5,3,6,4] #maxProfit
print(s.maxProfit(input_data))

input_data = ["eat", "tea", "tan", "ate", "nat", "bat"] #groupAnagrams
print(s.groupAnagrams(input_data))

input_data = [1,3,2,3,5,0] #countElements
print(s.countElements(input_data))