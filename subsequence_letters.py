def longestSubsequence(s):
  if not s:
    return 0
  
  hash = {}
  start = maxCount = 0
  for i in range(len(s)):
    let = s[i]
    if let in hash:
      maxCount = max(i - start,maxCount)
      start = max(hash[let] + 1,start)    
    hash[let] = i

  maxCount = max(len(s) - start,maxCount)
  return maxCount

longestSubsequence("abba")