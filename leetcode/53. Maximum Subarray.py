#53. Maximum Subarray
def maxSubArray(self, nums: list[int]) -> int:
    sum = 0
    maxi = float('-inf')
    i = j = 0
    while(j<len(nums)):
        if(sum < 0 and nums[j] >= sum):
            sum = 0
        sum += nums[j]
        maxi = max(maxi, sum)
        j+=1
    return maxi
    # biggest, big = nums[0],nums[0]
    # l = sum(nums)
    # #start of subarr is :x
    # for x in range(0,len(nums)):
        
    #     #gives end of subarr:y
    #     for y in range(x,len(nums)):

    #         #check for every digit between x & y (including y)
    #         subarr = nums[x:y+1]
    #         print(subarr)
    #         big = max(big,sum(subarr))
    
    #     if l > biggest:
    #         biggest = l
            
    #     biggest = max(big,biggest)
    #     print(big,biggest)
    # return biggest

print(maxSubArray(5,[-2,1,-3,4,-1,2,1,-5,4]))