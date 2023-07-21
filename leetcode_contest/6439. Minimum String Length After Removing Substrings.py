#6439. Minimum String Length After Removing Substrings
def subs(s):
    s = list(s)
    while True:
        n = 0
        if s[n] == 'A' and s[n+1] == 'B':
            s.pop(n)
            s.pop(n+1)
        else:
        if s[n] == 'C' and s[n+1] == 'D':
            s.pop(n)
            s.pop(n+1)
        if n == len(s):
            n = 0
        else:
            n += 1
    return len(s)

print(subs("ABFCACDB"))