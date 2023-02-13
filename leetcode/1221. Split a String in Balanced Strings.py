#1221. Split a String in Balanced Strings
def balancedStringSplit(self, s: str) -> int:
    d,left,right = 0,0,0
    for i in range(len(s)):
        if s[i] == 'L' :
            left +=1 
        else:
            right +=1
        if left == right and left != 0:
            d+=1
            left,right = 0,0
    return d

print(balancedStringSplit(5,"RLRRLLRLRL"))