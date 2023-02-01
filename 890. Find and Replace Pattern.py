#890. Find and Replace Pattern
def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
    x = drive_number(pattern)
    fin = []
    for i in words:
        if drive_number(i) == x:
            fin.append(i)
    return fin

def drive_number(k : str ):
    cart = []
    dem = []
    for i in range(len(k)):
        if k[i] not in cart:
            cart.append(k[i])
            dem.append(i)
        else :
            c = cart.index(k[i])
            dem.append(c)
    return dem
    
print(findAndReplacePattern(5,["abc","cba","xyx","yxx","yyx"],"abc"))