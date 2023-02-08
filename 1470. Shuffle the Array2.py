#1470. Shuffle the Array2
def shuffle(self, nums: list[int], n: int) -> list[int]:
    a = nums[:n]
    b = nums[n:]
    nums = []
    for i in range(n):
        nums.append(a[i])
        nums.append(b[i])

    return nums

print( shuffle(1, [2,5,1,3,4,7],3 ) )