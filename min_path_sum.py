def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 and col == 0:
                continue
            elif row == 0:
                grid[row][col] = grid[row][col] + grid[row][col-1]
            elif col == 0:
                grid[row][col] = grid[row-1][col] + grid[row][col]
            else:
                grid[row][col] = min(grid[row-1][col],grid[row][col-1]) + grid[row][col]
    return grid[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]

minPathSum(grid)