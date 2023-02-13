#1281. Subtract the Product and Sum of Digits of an Integer
def subtractProductAndSum(self, n: int) -> int:
    a = 1
    b = 0
    n = str(n)
    for i in n:
        print(i,a,b)
        a*=int(i)
        b+=int(i)
    return a-b

print(subtractProductAndSum(5,234))