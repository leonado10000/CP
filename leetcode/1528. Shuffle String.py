#1528. Shuffle String
def restoreString(self, s: str, indices: list[int]) -> str:
        a=""
        for i in indices:
            a+=s[i]
        return a

print(restoreString(5,"codeleet",[4,5,6,7,0,2,1,3]))