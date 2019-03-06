class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lists = [ [] * i for i in range(numRows) ]
        incrementer = 1
        i = 1
        length = len(s)
        lists[0].append(s[0])
        
        for j in range(1,length):
            lists[(i % numRows)].append(s[j])
            if i == (numRows-1) or i == 0:
                incrementer *= -1
            i += incrementer
        result = ''
        for array in lists:
            result += ''.join(array)
        return result


obj = Solution()
obj.convert("PAYPALISHIRING",3)