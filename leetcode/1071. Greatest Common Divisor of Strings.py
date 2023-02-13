#1071. Greatest Common Divisor of Strings
def gcdOfStrings(self, str1: str, str2: str) -> str:
    fin = ""
    m = min(len(str1),len(str2))
    gin = []
    for i in range(1,m+1):
        if len(str1)%i == 0 and len(str2) % i == 0:
            gin.append(i)
    
    for i in gin:
        #check for str1
        a = str2[0:i]
        if str1 == a*int(len(str1)/i) and str2 == a*int(len(str2)/i):
            fin = a
    
    return fin



print(gcdOfStrings(5,str1 = "ABCABC", str2 = "ABC"))