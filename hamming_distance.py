def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    xstr = bin(x)[2:]
    ystr = bin(y)[2:]
    
    diff = len(xstr) - len(ystr)
    if diff < 0:
        xstr = xstr.zfill(len(ystr))
    else:
        ystr = ystr.zfill(len(xstr))
    count = 0
    i = 0
    while i < len(xstr):
      if ystr[i] != xstr[i]:
        count += 1
      i += 1
    return count
    
    
        
hammingDistance(34,56)