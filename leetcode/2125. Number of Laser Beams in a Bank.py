#2125. Number of Laser Beams in a Bank
def numberOfBeams(self, bank: list[str]) -> int:
    numv = []
    for i in range(len(bank)):
        if int(bank[i]) == 0:
            continue
        numv.append(bank[i].count('1'))
    if len(numv) ==1:
        return 0
    t = 0
    for i in range(len(numv)-1):
        t += numv[i]*numv[i+1]
    return t

print(numberOfBeams(5,["011001","000000","010100","001000"]))