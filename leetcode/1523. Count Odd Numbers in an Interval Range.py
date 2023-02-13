#1523. Count Odd Numbers in an Interval Range
def countOdds(self, low: int, high: int) -> int:
    c = 0
    for x in range(low,high+1):
        c+=1
    return c
"""        if low%2!=0:
            if (high-low)%2==0:# if both are odd
                return  int(((high-low)+2)/2)
            else:# if only 1st is odd
                return int(((high-low)+1)/2)
        else:
            if (high-low)%2==0:# if both are even
                return  int(((high-low))/2)
            else:   # if only second is odd
                return int(((high-low)+1)/2)"""