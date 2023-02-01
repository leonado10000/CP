#5. Longest Palindromic Substring
def longestPalindrome(self, s: str) -> str:
    a,b=0,len(s)
    for i in range(0,len(s)):
        
        if i%2 == 0:
           
            a+=int(i/2)+1
            if ispalin(s[a:b]):
                return s[a:b]
        else:
            b-=int(i/2)+1
            if ispalin(s[a:b]):
                return s[a:b]

def ispalin(s):
    print(s)
    if len(s)%2 == 0:
        
        k = s[int(len(s)/2)+1:]
        k = k[len(k)-1:0]
        if s[:int(len(s)/2)] == k:
            return True
        else:
            return False
    else :
        k = int(len(s)/2)+1
        if s[:k] == s[k+1:]:
            return True
        else:
            return False

print(longestPalindrome(5,"babad"))