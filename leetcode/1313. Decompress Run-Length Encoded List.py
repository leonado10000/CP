#1313. Decompress Run-Length Encoded List
def decompressRLElist(self, nums: list[int]) -> list[int]:
    fin = []
    for i in range(1,len(nums)+1,2):
        fin += [nums[i]]*nums[i-1]
    return fin

print(decompressRLElist(5, [1,2,3,4]))