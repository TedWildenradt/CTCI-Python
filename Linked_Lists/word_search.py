class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def dfs(word,row,col):
            if not word:
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[0]:
                return False
            temp = board[row][col]
            board[row][col] = '#'
            
            if dfs(word[1:],row+1,col):
                return True
            if dfs(word[1:],row-1,col):
                return True
            if dfs(word[1:],row,col+1):
                return True
            if dfs(word[1:],row,col-1):
                return True
            board[row][col] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    status = dfs(word,i,j)
                    if status:
                        return True
        return False

obj = Solution()
# word = 'ABCCED'
# word = 'SEE'
word = 'ABCB'
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
obj.exist(board,word)

