def permutations_palidrome(string):
  array = [0] * 128
  count = 0
  for letter in string:
    array[ord(letter)] += 1
    if array[ord(letter)] % 2 == 1:
      count += 1
    else:
      count -= 1
  return count <= 1

permutations_palidrome('the')
