#567. Permutation in String
def checkInclusion(self, s1: str, s2: str) -> bool:
    L = giveper(list(s1),0,len(s1))
    for u in L:
        if u in s2:
            return True
            break
    return False


m = []
def giveper(x,y,z):
    if(y==z):
        m.append(perm(x))
    else:
        for i in range(y,z):
            x[y], x[i] = x[i], x[y]
            giveper(x,y+1,z)
            x[y], x[i] = x[i], x[y]
    return m

def perm(d):
    return ''.join(d)

print(checkInclusion(5,'asd','ajsdhaldjdsa'))