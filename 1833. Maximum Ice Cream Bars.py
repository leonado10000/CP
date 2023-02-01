#1833. Maximum Ice Cream Bars
def maxIceCream(self, costs: list[int], coins: int) -> int:
    costs.sort()
    seto = 0
    for i in costs:
        coins -= i 
        if coins <  0:
            break
        seto += 1
            
    return seto

print(maxIceCream(5,[1,6,3,1,2,5],20))