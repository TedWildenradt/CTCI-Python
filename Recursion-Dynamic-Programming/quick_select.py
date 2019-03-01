import random
def quickselect(arr, k):


  n = len(arr)
  low = 0
  high = n-1

  while low <= high:
    p = partition(arr, low, high)
    if p == n-k:
      return arr[p]
    elif p < n-k:
      low = p + 1
    else:
      high = p - 1

def partition(arr, low, high):
  i = low
  for j in range(low,high):
    if arr[j] <= arr[high]:
      arr[j], arr[i] = arr[i], arr[j]
      i += 1
  arr[i], arr[high] = arr[high], arr[i]
  return i 




quickselect([5,2,4,1,3,6,0],4)