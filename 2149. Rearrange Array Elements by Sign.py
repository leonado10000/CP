#2149. Rearrange Array Elements by Sign
def rearrangeArray(nums: list[int]) -> list[int]:
    posi , negi = [], []
    for i in nums:
        if i >= 0 :
            posi.append(i)
        else:
            negi.append(i)
    k = len(nums)
    nums = []
    for i in range(0,int(k/2)):
        nums.append(posi[i])
        nums.append(negi[i])
    return nums

print(rearrangeArray([3,1,-2,-5,2,-4]))