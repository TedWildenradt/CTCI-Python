class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowSet = [set() for i in range(9)]
        colSet = [set() for i in range(9)]
        boxSet = [set() for i in range(9)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num == '.':
                    continue
                if num in rowSet[row] or num in colSet[col] or num in boxSet[(row/3)*3+col/3]:
                    return False
                else:
                    rowSet[row].add(num)
                    colSet[col].add(num)
                    boxSet[(row/3)*3+col/3].add(num)
        return True

obj = Solution()
# obj.isValidSudoku([
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ])

obj.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])