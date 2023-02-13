#1282. Group the People Given the Group Size They Belong To
def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
    fin = []
    gp = groupSizes
    for i in gp:
        temp = []
        i = str(i)
        if i.isnumeric():
            i = int(i)
            for j in range(0,len(groupSizes)):
                if len(temp)>=i:
                    break
                else:
                    a = groupSizes[j]
                    if a==i :
                        temp.append(j)
                        gp[j] = ""
            fin.append(temp)
    return fin

print(groupThePeople(5,[2,1,3,3,3,2]))