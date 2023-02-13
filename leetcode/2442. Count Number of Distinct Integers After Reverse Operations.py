#2442. Count Number of Distinct Integers After Reverse Operations
def countDistinctIntegers( nums: list[int]) -> int:
    k = nums
    for i in nums:
        e = str(i)
        r = e[-1:]
        r = int(r)
        k.append(r)
    u = len(set(nums))
    return u
print(countDistinctIntegers([1,13,10,12,31]))