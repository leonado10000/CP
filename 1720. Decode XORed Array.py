#1720. Decode XORed Array
def decode(self, encoded: list[int], first: int) -> list[int]:
    ans = []
    ans.append(first)
    for i in range(0,len(encoded)):
        if i != 0:
            ans.append(encoded[i] - ans[i])
        else:
            ans.append(0)
    return ans

#print(decode(5,encoded = [6,2,7,3], first = 4))
sw = (4 and not 2) or (not 4 and 2)
print(sw)  