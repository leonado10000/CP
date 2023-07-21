# 6470. Neither Minimum nor Maximum
def findNonMinOrMax(self, nums: list[int]) -> int:
    nums = set(nums)
    if len(nums)>2:
        nums = list(nums)
        nums.sort()
        return nums[1]
    else:
        return -1
print(findNonMinOrMax(4,[2,25,4]))