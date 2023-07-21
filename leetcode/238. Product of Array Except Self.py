# 238. Product of Array Except Self
def productExceptSelf(self, nums: list[int]) -> list[int]:
    product = 1
    n=0
    if nums.count(0) >=2:
        return [0]*len(nums)
    for i in nums:
        if i == 0:
            n =1
            pos = nums.index(0)
            continue
        product *= i
    yli = []
    if n==0:
        for i in nums:
            yli.append(int(product/i))
    else:
        yli = [0]*len(nums)
        yli[pos]=product

    return yli

print(
    productExceptSelf(
        1,
        [-1,1,0,-3,3]
    )
)
