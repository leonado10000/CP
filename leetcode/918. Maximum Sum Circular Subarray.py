#918. Maximum Sum Circular Subarray
def maxSubarraySumCircular(self, nums: list[int]) -> int:
    biggest, big = nums[0],nums[0]
    l = sum(nums)
    #start of subarr is :x
    for x in range(0,len(nums)):
        
        #gives end of subarr:y
        for y in range(x,len(nums)):

            #check for every digit between x & y (including y)
            subarr = nums[x:y+1]
            print(subarr)
            big = max(big,sum(subarr))

            #incase it reaches last index
            if y == len(nums)-1:
                for z in range(0,x):
                    subarr = nums[x:] + nums[0:z]
                    print("specsh",subarr)
                    big = max(big,sum(subarr))
                
        if l > biggest:
            biggest = l
            
        biggest = max(big,biggest)
        print(big,biggest)
    return biggest

print(maxSubarraySumCircular(5,[3,1,3,2,6]))