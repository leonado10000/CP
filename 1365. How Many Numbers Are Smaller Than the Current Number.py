#1365. How Many Numbers Are Smaller Than the Current Number
def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    k = nums
    k.sort()
    fin = []
    low=0 
    high=len(nums)-1
    for i in nums:
        while low < high :
            mid = (low + high)/2
            if k[mid] == i :
                for k in range(0,mid):
                    if k[mid-i] 
                break