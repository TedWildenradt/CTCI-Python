def one_away(str1,str2):
  intersection = (set(str1).difference(set(str2)))
  return len(intersection) == 1

one_away('pale', 'bake')
one_away('pale', 'bale')
