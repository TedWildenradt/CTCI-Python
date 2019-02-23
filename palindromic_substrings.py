def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    count = 0
    for i in range (len(s)):
      count += helper(s,i,i)
      count += helper(s,i,i+1)
    return count
    
def helper(s,l,r):
    count = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        count += 1
    return count

countSubstrings('aaa')