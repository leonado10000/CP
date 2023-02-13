#22. Generate Parentheses
def generateParenthesis(self, n: int) -> list[str]:
    d = []
    def cool(left,right,s):
        if len(s)==2*n and left == right:
            d.append(s)
            return
        print(left,right)
        if left < n:
            left += 1
            for i in range(left,n+1):
                print("left\t",i,right,s+"(")
                cool(i,right,s+"(")
        
        if right < 1+ left:
            right += 1
            for i in range(right,left+1):
                print("right\t",left,i,s+")")
                cool(left,i,s+")")

    cool(0,0,"")
    return d

print(generateParenthesis(5,2))