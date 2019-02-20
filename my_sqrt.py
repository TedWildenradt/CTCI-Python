def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 1:
      return 1
    left = 0
    right = x
    
    while left <= right:
        mid = (right+left) // 2
        if mid * mid <= x < (mid+1) * (mid+1):
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

mySqrt(55)