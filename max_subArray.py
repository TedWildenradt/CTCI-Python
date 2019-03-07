def maxSubArray(nums):
  if not nums:
    return 0
  maxSum = float('-inf')
  currSum = float('-inf')

  for num in nums:
    maxSum = max(maxSum, currSum)
    currSum = max(num, currSum + num)
  return max(maxSum, currSum)

maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) #6
maxSubArray([-2,-3,-4]) #6
