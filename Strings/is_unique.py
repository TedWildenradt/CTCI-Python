def is_unique(string):
  if len(string) > 128:
    return False
  holder = set()
  for i in string:
    if i in holder:
      return False 
    else:
      holder.add(i)
  return True 

is_unique('asdfwera') #False
is_unique('asdfwer') #True