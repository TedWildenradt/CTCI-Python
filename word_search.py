def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    def search(row,col,w,visited=set()):
        
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row,col) in visited or board[row][col] != w[0]:
            return False
        if len(w) == 1:
            return True
        
        visited.add((row,col))
        
        return search(row+1,col,w[1:],visited) or search(row-1,col,w[1:],visited) or search(row,col+1,w[1:],visited) or search(row,col-1,w[1:],visited)
        
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                visited = set()
                status = search(i,j,word,visited)
                if status:
                    return True
    return False

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
exist(board,"AAB")