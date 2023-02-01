#131. Palindrome Partitioning
def partition(self, s: str) -> list[list[str]]:
    end = []

    def issub(n,k):
        if n == len(s) :
            end.append(k)
            print(end)
            return
        for g in range(n, len(s)):
            x = s[n:g+1]
            if palin(x):
                issub(g+1,k + [x])
        return

    def palin(a):
        return a == a[::-1]
        
    issub(0,[])
    return end
"""        lst = []
        def palindrome(a):
            return a == a[::-1]
        def dfs(i,curr):
            if i == len(s):
                lst.append(curr)
                return 
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if palindrome(sol):
                    dfs(j+1, curr + [s[i:j+1]])
            return 
        dfs(0,[])
        return lst

"""  
print(partition(5,"aab"))