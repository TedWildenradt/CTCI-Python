class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        heights = [0] * (buildings[-1][1] + 1)
        
        for building in buildings:
            for i in range(building[0], building[1]):
                heights[i] = max(heights[i],building[2])
        output = []
        i = 0

        while heights[i] == 0:
                i += 1

        while i < len(heights):

            output.append([i,heights[i]])
            while i < len(heights) - 1 and heights[i] == heights[i+1]:
                i += 1
            i += 1
        return output


obj = Solution()
obj.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])