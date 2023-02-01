#2535. Difference Between Element Sum and Digit Sum of an Array
def differenceOfSum(self, nums: list[int]) -> int:
    a = 0
    for x in nums:
        if x>9:
            g = 0
            if x>99:
                if x>999:#more than 999         4 digit
                    x = str(x)
                    g = int(int(x[0])+int(x[1])+int(x[2])+int(x[3]))
                    x = int(x)
                else: #betweeen 99 and 999      3 digit
                    x = str(x)
                    g = int(int(x[0])+int(x[1])+int(x[2]))
                    x = int(x)
            else:#between 9 and 99              2 digit
                x = str(x)
                g = int(int(x[0])+int(x[1]))
                x = int(x)

            a += (x - g)
    return a

print(differenceOfSum(5,[1,15,6,3]))