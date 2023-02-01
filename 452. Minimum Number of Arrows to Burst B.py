#452. Minimum Number of Arrows to Burst Balloons
def findMinArrowShots(self, points: list[list[int]]) -> int:
    get = 1
    points.sort(key=lambda x:x[1])
    print(points)
    l,r =points[0][0],points[0][1]
    for x in points:
        if x[0]>r:
            r=x[1]
            get+=1
    return get

print(findMinArrowShots(5,[[1,2],[3,4],[5,6],[7,8]]))