#2530. Maximal Score After Applying K Operations
import math
def maxKelements(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        score = 0
        for i in range(k):
            score += nums[0]
            nums[0] = math.ceil(nums[0]/3)
            for x in range(0,len(nums)):
                if nums[0] > nums[x]:
                    nums = nums[1:x] + [nums[0]] + nums[x:]
                    break
        return score
    

print(maxKelements(5,[10,10,10,10,10],5))
