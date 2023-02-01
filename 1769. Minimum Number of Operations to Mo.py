#1769. Minimum Number of Operations to Move All Balls to Each Box
def minOperations(self, boxes: str) -> list[int]:
    ans = []
    temp = []
    for n,x in enumerate(boxes):
        if x=="1":
            temp.append(n)
    print(temp)
    for c in range(0,len(boxes)):
        t = 0
        for j in temp:
            if j - c > -1:
                t += (j-c)
            else:
                t +=  (c-j)
        ans.append(t)
    return ans

"""    for n,x in enumerate(boxes):
        i = 0
        pintu = 0
        if n == 0 :
            i = 1
        while(i < len(boxes)):
            nux=0
            if ( i != n and boxes[i]=="1" ):
                nux = n - i
                if nux < 0:
                    nux=-nux
            pintu += nux
            i+=1

        ans.append(pintu)
    
    return ans"""

print(minOperations(5,"110"))