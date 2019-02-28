import collections
def maxSlidingWindow(nums, k):
    dq,ans = collections.deque(),[]
    for i,n in enumerate(nums):
        while dq and (i-k >= dq[0] or n >= nums[dq[0]]):
            dq.popleft()
        while dq and n >= nums[dq[-1]]:
            dq.pop()
        dq += i,
        if i >= k-1:
            ans += nums[dq[0]],
    return ans

maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)