#1061. Lexicographically Smallest Equivalent String
def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    a = list(zip(s1,s2))
    for i in range(len(a)):
        a[i] = list(a[i])
    z = []  #already mapped
    for x in range(len(a)):
        for y in a[x]:
            check = 0
            for i in range(0,x):
                if y in a[i]:
                    a[i] += a[x]
                    a[i].sort()
                    a[i] = list(set(a[i]))
                    a[x] = ""
                    
                    check = 1
                    break
            if check == 1:
                break
    for i in range(a.count("")):
        a.remove("")
    print(a)
        
    fin = ""        
    g = []
    for x in range(len(baseStr)):
        g.append(x)
        for i in range(len(a)):
            if baseStr[x] in a[i]:
                fin += a[i][0]
                g.pop()
                flag = 1
                break
    for i in g:
        fin = fin[:i] + baseStr[i] +fin[i:]

    
    return fin

print(smallestEquivalentString(5,"gicimlheddadmbmhiimakmhgklliljllfgjegamichefljcdef","jgjbjkhkliegkfdcbfcdgmeadlkgcdfkcjdmmcgliegijgjimj","lqppdcmgachdannbaeztqoqfpimyzcdqksykgwymceogkgruey"))