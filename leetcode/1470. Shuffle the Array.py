#1470. Shuffle the Array
def shuffle(self, nums: list[int], n: int) -> list[int]:
    x = nums[:n]
    y = nums[n:2*n]
    nums = []
    for i in range(n):
        nums.append(x[i])
        nums.append(y[i])
    return nums

print( shuffle(1, [2,5,1,3,4,7],3 ) )

#version 2 : better
"""      nu = nums
        nums = []
        for i in range(n):
            nums.append(nu[i])
            nums.append(nu[n+i])
        return nums """