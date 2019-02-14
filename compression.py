def compression(string):
  output = ""
  curr = string[0]
  count = 1
  for i in range(1, len(string)):
    if string[i] == curr:
      count += 1
    else:
      output += curr + str(count)
      curr = string[i]
      count = 1
  output += curr + str(count)

  return output 

compression('aabcccccaaa')
compression('abbbccd')