def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length = 0
    output = ''
    for i in range(len(s)):
        possible = helper(s,i,i)
        if len(possible) > length:
            output = possible
            length = len(possible)
        possible = helper(s,i,i+1)
        if len(possible) > length:
            output = possible
            length = len(possible)
    return output
        
            
    
def helper(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

helper('babad',2,2)