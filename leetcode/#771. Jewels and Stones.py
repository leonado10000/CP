#771. Jewels and Stones
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        for i in jewels:
            c += stones.count(i)
        return c

print(numJewelsInStones(5,jewels = "aA", stones = "aAAbbbb"))