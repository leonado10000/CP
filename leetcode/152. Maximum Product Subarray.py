# 152. Maximum Product Subarray

def maxProduct(self, nums: list[int]) -> int:
    if len(nums)==1:
        return nums[0]
    maxi = float('-inf')
    temp = []
    prod = 1
    yes = 0
    for n,x in enumerate(nums[:]):
        if x==0 or prod==0:
            prod = 1
            yes = 1
        else:
            if x <0 :
                for m,i in enumerate(temp):
                    temp[m] = i*x
                temp.append(x)
                # maxi = max(max(temp),maxi)
            prod *= x
            maxi = max(prod,maxi,x)
    print(temp)
    a = temp.index(max(temp))
    jail  = max(temp)
    for x in nums[len(temp)+a:]:
        jail *= x
    if yes:
        return max(maxi,0,jail)
    else:
        return max(jail,maxi)


print(maxProduct(2,[1,0,-1,2,3,-5,-2]))