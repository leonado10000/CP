#1637. Widest Vertical Area Between Two Points Containing No Points
def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
    x = [i[0] for i in points]
    maxi = 0
    x.sort()
    for i in range(0,len(x)-1):
        if (x[i+1] - x[i] > maxi):
            maxi = x[i+1] - x[i]
    return maxi
    
print(maxWidthOfVerticalArea(5,[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))