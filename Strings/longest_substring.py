def lengthOfLongestSubstring(s):

  if len(s) <= 1:
    return len(s)
  tracker = {}
  longest = 0
  start = 0

  for i,curr in enumerate(s):
    if curr in tracker:
      longest = max(longest,i - start)
      start = max(start,tracker[curr] + 1)
    tracker[curr] = i
  return max(longest, len(s) - start)


lengthOfLongestSubstring('pwwekwe')

