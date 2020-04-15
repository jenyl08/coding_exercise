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

    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """

        self.isAlready = set([])

        def hn(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                sum = 0
                while n >= 10:
                    s = n % 10
                    sum = sum + s * s
                    n = int(n / 10)
                sum = sum + n * n
                if sum in self.isAlready:
                    return 0
                else:
                    self.isAlready.add(sum)
                    return hn(sum)

        if hn(n) == 1:
            return True
        else:
            return False

s=Solution()

input_data = 19 #isHappy
print(s.isHappy(input_data))

input_data = 19 #isHappy2
print(s.isHappy2(input_data))