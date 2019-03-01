def findKthLargestPartition(nums, k):
  start = 0
  end = len(nums) - 1
  rank = len(nums) - (k-1)

  while start <= end:
    ret = partition(nums, start, end)
    if ret == rank - 1:
      return nums[ret]
    elif ret < rank - 1:
      start = ret + 1
    else:
      end = ret - 1

def partition(nums, start, end):
  pivot = start 

  while start < end:
    while nums[end] > nums[pivot] and end > start:
      end -= 1
    while nums[start] <= nums[pivot] and start < end:
      start += 1

    nums[start], nums[end] = nums[end], nums[start]

  nums[pivot], nums[start] = nums[start], nums[pivot]

  return start 

findKthLargestPartition([3,2,1,5,6,4],2)