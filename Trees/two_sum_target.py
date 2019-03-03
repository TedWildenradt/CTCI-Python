def twoSumTarget(array, target):
  possibles = set()
  for num in array:
    if target - num in possibles:
      return True
    else:
      possibles.add(num)
  return False

twoSumTarget([10, 15, 3, 7],17)