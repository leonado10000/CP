#899. Orderly Queue
def orderlyQueue(self, s: str, k: int) -> str:
    if len(s) < 3:
        if len(s) == 1 or len(s) == 0:
            return s
        else:
            if s[0] <= s[1]:
                return s
            else:
                return s[1]+s[0]
    else:
        side_string = s[:k]
        l_string = []
        for i in side_string:
            l_string.append(i)
        l_string.sort(reverse=True)
        