def merge_sorted_array(A,B,n):
  end = len(A) - 1
  end_a = len(A) - n - 1
  while B:
    b_val = B[-1]
    a_val = A[end_a]
    if b_val >= a_val:
      A[end] = B.pop()
    else:
      A[end],A[end_a] = A[end_a], A[end]
      end_a -= 1
    end -= 1
  return A 
x = float('-inf')
A = [1,5,6,9,float('-inf'),float('-inf'),float('-inf'),float('-inf')]
B = [3,4,7,10]
merge_sorted_array(A,B,4)