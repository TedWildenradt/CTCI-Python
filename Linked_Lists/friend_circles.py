class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.output = 0
        self.visited = set()
        
        def dfs(j):
            self.visited.add(j)
            for connection in range(len(M[j])):
                if M[j][connection] == 1 and connection not in self.visited:
                    dfs(connection)
        
        for i in range(len(M)):
            if i in self.visited:
                continue
            for j in range(len(M[0])):
                if j in self.visited:
                    continue
                if M[i][j] == 1 and i not in self.visited and j not in self.visited:
                    self.visited.add(i)
                    dfs(j)
                    self.output += 1
                    
        return self.output

M = [[1,1,0],[1,1,1],[0,1,1]]
obj = Solution()
obj.findCircleNum(M)