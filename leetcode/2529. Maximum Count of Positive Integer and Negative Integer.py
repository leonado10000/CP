#2529. Maximum Count of Positive Integer and Negative Integer
def maximumCount(self, nums: list[int]) -> int:
        n,p = 0,0
        for i in range(len(nums)):
            if nums[i] >= 0 and nums[i-1] < 0:
                print(nums[i])
                n = i
            if nums[i] > 0:
                p = len(nums)-i
                break
        return max(n,p)

print(maximumCount(5, [-3,-2,-1,0,0,1,2]))