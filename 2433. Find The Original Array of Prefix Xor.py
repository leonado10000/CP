#2433. Find The Original Array of Prefix Xor
def findArray(self, pref: list[int]) -> list[int]:
    fin = [pref[0]]
    for i in range(1,len(pref)):
        s,q = pref[i],pref[i-1]
        an = s^q
        fin.append(an)

    return fin

print(findArray(5,[5,2,0,3,1]))