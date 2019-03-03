# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        output = [intervals[0]]
        for interval in intervals[1:]:
            if self.overlapping(output[-1],interval):
                output[-1] = self.merge2(output[-1],interval)
            else:
                output.append(interval)
        return output
        
        
    def overlapping(self, int1, int2):
        if int1.end < int2.start:
            return False
        else:
            return True
    
    def merge2(self,int1, int2):
        return Interval(min(int1.start,int2.start),max(int1.end,int2.end))


arr = [[1,3],[2,6],[8,10],[15,18]]
intervals = []
for int in arr:
  newInt = Interval(int[0],int[1])
  intervals.append(newInt)

obj = Solution()
obj.merge(intervals)