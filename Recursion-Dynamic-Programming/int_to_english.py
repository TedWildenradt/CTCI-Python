class Solution(object):

    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        
        newString = ''
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                newString = self.helper(num % 1000)  + self.thousands[i] + ' ' + newString
            else:
                return newString.strip()
            num = num // 1000
        return newString.strip()
        
    def helper(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.lessThan20[num] + ' '
        elif num < 100:
            return self.tens[num/10] + ' ' + self.helper(num % 10)
        else:
            return self.lessThan20[num/100] + ' Hundred ' + self.helper(num % 100)

obj = Solution()
obj.numberToWords(50868)