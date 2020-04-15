class Solution(object):
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
s=Solution()

input_data = 19 #isHappy
print(s.isHappy(input_data))