#944. Delete Columns to Make Sorted
def minDeletionSize(self, strs: list[str]) -> int:
    return (zip(strs))
#    count = 0
#    for i in range(len(strs[0])):
#        for j in range(len(strs)-1):
#            print(strs[j][i],ord(strs[j][i]),strs[j+1][i],ord(strs[j+1][i]))
#            if ord(strs[j][i]) > ord(strs[j+1][i]) :
#                count += 1
#                break
#    return count
print(minDeletionSize(5,["zyx","wvu","tsr"]))