import re
def urlify(string):
  string = string.strip()
  arr = string.split(' ')
  return '%20'.join(arr)

urlify('     ss ad f   ')
