#44. Wildcard Matching
def isMatch(self, s: str, p: str) -> bool:
    if "*" not in p and "?" not in p:
        return s == p

    for i in range(0,len(p)):
        if s[i] == p[i]:
            continue
        elif p[i] == "*" and p.index(p[i]) == len(p)-1:
            return True
        elif p[i] == "?":
            continue
        else:
            return False

print(isMatch(5,"aa","?x*"))