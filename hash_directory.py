def hash_directory(files):
  if not files:
    return []
  output = []

  def helper(hash, path=''):
    for file in hash.keys():
      if hash[file] == True:
        output.append(path+file)
        return
      helper(hash[file],path+file)

  
  for file in files.keys():
    helper(files[file],file)
  
  res = []
  for path in output:
    res.append('/'.join(list(path)))
  return res

files = {
  'a' : {
    'b' : {
      'c' : {
        'd' : {
          'e' : True
        },

        'f' : True
      }
    }
  }
}

hash_directory(files)
