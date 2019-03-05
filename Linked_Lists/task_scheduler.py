from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = {}
        for task in tasks:
            counter[task] = counter.get(task,0) + 1
        idle = 0
        
        while counter:
            length = len(counter)
            for key in counter.keys():
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
                
            if not counter:
                break
            idle += (n - length + 1)
            
        if idle <= 0:
            return len(tasks)
                
        return len(tasks) + idle

# tasks = ["A","A","A","B","B","B"]
tasks = ["A","A","A","A","B","C","D","E"]
n = 2

obj = Solution()
obj.leastInterval(tasks,n)