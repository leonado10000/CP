# 1498. Number of Subsequences That Satisfy the Given Sum Condition
def numSubseq(self, nums: list[int], target: int) -> int:
    mod = 10**9 + 7
    nums.sort()
    l = nums[0]
    r = 0
    sol = 0
    temp = [l]
    for i in range(1,nums):
        if max(temp) + min(temp) <= target:
            r = i
        else:
            r = r-1
