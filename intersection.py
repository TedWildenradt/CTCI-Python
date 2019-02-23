def intersection(i,j):
  left = max(i[0],j[0])
  right = min(i[1],j[1])
  return (left,right) if left < right else None 

# def intersections(A,B):
#   result = []
#   for i in A:
#     for j in B:
#       k = intersection(i,j)
#       if k is not None:
#         result.append(k)
#   return result

a1 = [(1,2),(3,4),(7,10)]
a2 = [(0,2),(3,8),(9,12)]

# intersections(a1,a2)

def intersections2(A,B):
  result = []
  i = 0
  j = 0
  while i < len(A) and j < len(B):
    k = intersection(A[i],B[j])
    if k is not None:
      result.append(k)
    if A[i][1] < B[j][1]:
      i += 1
    else:
      j += 1
  return result


intersections2(a1,a2)

