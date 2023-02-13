#1480. Running Sum of 1d Array
def runningSum(self, nums: list[int]) ->list[int]:
    ans = [nums[0]]
    for i in nums[1:]:
        ans = ans + [ans[-1]+i]
    return ans

print(runningSum(5,[1,2,3,4]))