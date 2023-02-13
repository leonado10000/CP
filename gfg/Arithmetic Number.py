def inSequence(self, A, B, C):
    if C>0:
        if B<A:
            return 0
        elif B==A:
            return 1
        else:
            if (B-A)%C == 0:
                return 1
            else:
                return 0
    elif C==0:
            if A==B:
                return 1
            else:
                return 0
    else:
        if B>A:
            return 0
        elif B==A:
            return 1
        else:
            if (B-A)%C == 0:
                return 1
            else:
                return 0
        
print(inSequence(1,-2,-9,-7))