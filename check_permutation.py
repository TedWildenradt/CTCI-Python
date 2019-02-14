def check_permutation(str1, str2):
  if len(str1) != len(str2):
    return False
  hash = {}
  for i in str1:
    hash[i] = hash.get(i,0) + 1
  for j in str2:
    if hash.get(j,0) == 0:
      return False 
    hash[j] -= 1
      
  return True

check_permutation('abcd','cbda')
check_permutation('dcw4f', 'dcw5f')
