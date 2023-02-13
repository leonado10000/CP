#149. Max Points on a Line
def maxPoints(self, points: list[list[int]]) -> int:
    points.sort(key=lambda x:x[0]+x[1])
    print(points)
    mai = 0
    for x in range(len(points)):
        for y in range(x+1,len(points)-1):
            temp = 0
            a = points[x]
            b = points[y]
            m = (b[1]-a[1])
            n = (b[0]-a[0])
            for j in range(0,len(points)):
                if (points[j][1] - b[1])*n == m*(points[j][0] - b[0]):
                    temp += 1
                    print(temp)
            mai = max(mai,temp)
    return mai

print(maxPoints(5,[[0,0],[0,1]]))