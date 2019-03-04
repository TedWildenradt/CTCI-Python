class Solution:
  def minWindow(self,s,t):
    left = 0
    right = 0
    comparable = {}
    hash = {}
    for i in range(len(t)):
      hash[t[i]] = 0
      comparable[t[i]] = comparable.get(t[i],0) + 1
    minWindowSize = float('inf')
    minWindow = []
    if s[0] in hash:
      hash[s[0]] += 1
    while right < len(s):
      if all(map(lambda k: hash[k] >= comparable[k], hash.keys())):
        if right - left < minWindowSize:
          minWindow = [left,right]
          minWindowSize = right - left 
        if s[left] in hash:
          hash[s[left]] -= 1
        left += 1
      else:
        right += 1
        if right < len(s) and s[right] in hash: 
          hash[s[right]] += 1
    if not minWindow:
      return ''
    else:
      return s[minWindow[0]: minWindow[1] + 1]

S = "ADOBECODEBANC"
T = "ABC"
obj = Solution()
obj.minWindow(S,T)