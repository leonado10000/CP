# 217. Contains Duplicate
def containsDuplicate(self, nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

print(
    containsDuplicate(
        1,
        [1,5,-2,-4,0]
        )
    )