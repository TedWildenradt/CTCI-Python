def lowestPositive(array):
  j = 0
  for i in range(len(array)):
    if array[i] <= 0:
      array[j], array[i] = array[i], array[j]
      j += 1

  for i in range(len(array)):
    if abs(array[i]) - 1 < len(array) and array[abs(array[i]) - 1] > 0:
      array[abs(array[i]) - 1] *= -1

  for i in range(len(array)):
    if array[i] > 0:
      return i + 1


lowestPositive([3, 4, -1, 1])