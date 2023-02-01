#2194. Cells in a Range on an Excel Sheet
def cellsInRange(self, s: str) -> list[str]:
    x1,x2 = ord(s[0]),ord(s[3])
    y1,y2 = int(s[1]),int(s[4])

    ans = []

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            a = str(chr(i))
            b = str(j)
            ans.append(a+b)

    return ans

print(cellsInRange(5,"K1:L2"))