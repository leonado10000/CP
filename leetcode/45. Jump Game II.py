#45. Jump Game II
def jump(self, nums: list[int]) -> int:
    count = 1
    point = 0
    #n points to current place in nums
    while(nums[point]+1+point<len(nums)):
        print("point=",point,"\tnums=",nums)
        count += 1
        Apparen = nums[point+1:nums[point]+1+point]
        real = []
        for i in range(0,len(Apparen)):
            real.append(Apparen[i]+i)

        print("Appenrent=",Apparen,"\treal=",real)
        k = max(real)
        point = real.index(k)+1+point
    return count

print(jump(5,[2,3,0,1,4]))


        #       4   1   3   1   2   1   7   1   1
        #       4   .   3   .   .   J  7.J  1   1
        #       4   .   .   .   2   .   J   .   .