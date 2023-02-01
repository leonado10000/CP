#1431. Kids With the Greatest Number of Candies
def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    ken = []
    ben = max(candies)
    for i in candies:
        if i+extraCandies >= ben :
            ken.append(True)
        else:
            ken.append(False)
    return ken

print(kidsWithCandies(5,[2,3,5,1,3],3))
