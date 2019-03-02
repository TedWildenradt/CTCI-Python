def findDuplicate(nums):
    n = len(nums) - 1
    expected = ((n)*(n+1))/2
    actual = sum(nums)
    return actual - expected

findDuplicate([1,3,4,2,2])