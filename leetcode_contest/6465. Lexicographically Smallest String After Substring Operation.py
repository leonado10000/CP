# 6465. Lexicographically Smallest String After Substring Operation
import string
def smallestString(self, s: str) -> str:
        # to find all positions of 'a'
        alpha = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:"z"}
        inv_map = {v: k for k, v in alpha.items()}
        a_index = []
        for n,a in enumerate(s):
            if a == 'a':
                a_index.append(n)
        
        ans = ''
        if a_index == []:
            for i in s:
                ans += alpha[inv_map[i]-1]
        elif len(a_index)==1:
            if (len(a_index) - 0) >= (len(s)-len(a_index)):
                for i in s[:a_index[0]]:
                    ans += alpha[inv_map[i]-1]
                ans += s[a_index[0]:]
        else:
            maxSortedAdjacentDiff([0]+a_index+[len(a_index)],len(a_index)+2)
