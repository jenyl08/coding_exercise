class Solution(object):
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

input_data = [1,3,2,3,5,0] #countElements
print(s.countElements(input_data))