#263. Ugly Number
def isUgly(self, n: int) -> bool:
    flag = 0
    if n < 0:
        flag = 1
    while n>1 :
        print(n)
        if n%5 == 0:
            n = n/5
        elif n%3 == 0:
            n = n/3
        elif n%2 == 0:
            n = n/2
        else:
            print("break")
            flag = 1
            break
        print(n)
    if flag == 0:
        return True
    else:
        return False

print(isUgly(5,14))