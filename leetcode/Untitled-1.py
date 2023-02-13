#1365. How Many Numbers Are Smaller Than the Current Number
def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    ans = []
    repeat1 = []
    repeat2 = []
    for i in range(0,len(nums)):
        k = 0
        if nums[i] not in repeat1:
            for j in range(0,len(nums)):
                if nums[i] > nums[j]:
                    k+=1
            ans.append(k)
            repeat1.append(i)
            repeat2.append(k)
        else:
            k = repeat1[i]
            ans.append(k)
    return ans

print(smallerNumbersThanCurrent(5,[8,55,2,2,3]))