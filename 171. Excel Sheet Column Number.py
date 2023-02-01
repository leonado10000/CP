#171. Excel Sheet Column Number 
def titleToNumber(self, columnTitle: str) -> int:
    x = len(columnTitle)
    krazy = 0
    j = x-1
    for i in columnTitle:
        the = ord(i) - 64
        krazy += the*(26**j)
        j -= 1
    return krazy

print(titleToNumber(5,"AAA"))