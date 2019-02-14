def zero_matrix(grid):
  rows = set()
  cols = set()
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == 0:
        rows.add(row)
        cols.add(col)
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if row in rows or col in cols:
        grid[row][col] = 0
  return grid

zero_matrix([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ])
