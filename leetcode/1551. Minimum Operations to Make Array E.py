#1551. Minimum Operations to Make Array Equal
def minOperations(self, n: int) -> int:
    cuss = []
    for i in range(0,n):
        cuss.append(2*i+1)
    if n%2 == 0:
        centre = cuss[int(n/2)]-1
    else:
        centre = cuss[int(n/2)]
    kello = 0
    if n%2 == 0:
        for i in range(0,int(n/2)):
            diff = centre - cuss[i]
            kello += diff
    else:
        for i in range(0,int(n/2)):
            diff = centre - cuss[i]
            kello += diff
    return kello
print(minOperations(5,3))