#1389. Create Target Array in the Given Order
def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
    fin = []
    for i in range(0,len(nums)):
        fin.insert(index[i],nums[i])
    return fin

print(createTargetArray(5,[0,1,2,3,4],[0,1,2,2,1]))