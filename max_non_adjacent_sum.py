def max_sum(nums):
  prevOne, prevTwo, ouput = 0,0,0
  for i in range(len(nums)):
    if i == 0:
      output = nums[0]
    elif i == 1:
      output = max(nums[0],nums[1])
    else:
      output = max(prevOne,nums[i] + prevTwo)
    prevTwo = prevOne
    prevOne = output
  return output

# max_sum([2,4,6,2,5]) #13
max_sum([5,1,1,5]) #10