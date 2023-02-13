#1523. Count Odd Numbers in an Interval Range
def countOdds(self, low: int, high: int) -> int:
    if low%2!=0:
        if (high-low)%2==0:
            return  ((high-low)+2)/2
        else:
            return ((high-low)+1)/2
    else:
        if (high-low)%2==0:
            return  ((high-low)+1)/2
        else:
            return ((high-low))/2