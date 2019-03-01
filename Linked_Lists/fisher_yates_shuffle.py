import random
def shuffle(array):
  length = len(array)
  end = length - 1

  for i in range(end,0,-1):
    j = random.randint(0,i)
    if i == j:
      continue
    array[j], array[i] = array[i],array[j]
  return array

shuffle([1,2,3,4,5])