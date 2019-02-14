def string_rotation(str1,str2):
  i = 0
  while str2[i] != str1[0]:
    i +=1
    if i >= len(str2):
      return False
  str3 = str2[i:] + str2[:i]
  return str3 in str1 

string_rotation('waterbottle','erbottlewat')
string_rotation('foo','bar')
string_rotation('foo','foofoo')