#15. 3Sum
def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        def bina(arr,key):
            l , r = 0, len(arr)-1
            while(l<=r):
                mid = (l+r)//2 
                if key > arr[mid]:
                    l = mid+1
                elif key< arr[mid]:
                    r = mid-1
                else:
                    return 1
            return -1
        print("yes")
        for i in range(len(nums)-2):
            x = nums[i]
            for j in range(i+1,len(nums)-1):
                y = nums[j]
                c = -x -y

                if bina(nums[j+1:],c)!=-1:
                    res.append([x,y,c])
       
        return res
        # fin = []

        # gastro = set(nums)
        # gastro = list(gastro)
        # nums.sort()
        # for i in gastro:
        #     if i in nums:
        #         nums.remove(i)
        # gastro.sort()
        # #now we have two lists
        # #1. with unique numbers
        # #with extra of uniques

        # #route one with inly sets
        # for i in range(0,len(gastro)-2):
        #     for j in range(i,len(gastro)-1):
        #         c = -gastro[i] -gastro[j]
        #         if c in gastro[j+1:]:
        #             fin.append([gastro[i],gastro[j],c])
        
        # for k in range(0,len(fin)):
        #     fin[k].sort()
        # #return all unique answers
        # for i in range(0,len(nums)-1):
        #     c = -nums[i] - nums[i+1]
        #     if c in gastro:
        #         if [nums[i],nums[i+1],c] not in fin:
        #             fin.append([nums[i],nums[i+1],c])

print(threeSum(5, [-1,0,1,2,-1,-4]),3)