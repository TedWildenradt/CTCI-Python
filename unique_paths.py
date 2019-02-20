def uniquePaths(m,n):
  matrix = []
  firstRow = [1] * m
  matrix.append(firstRow)
  for i in range(1,n):
    newRow = [1]
    for j in range(1,m):
      square = matrix[-1][j] + newRow[-1]
      newRow.append(square)
    matrix.append(newRow)
  return matrix[-1][-1]



uniquePaths(7,3)