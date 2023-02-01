#2244. Minimum Rounds to Complete All Tasks
def minimumRounds(self, tasks: list[int]) -> int:
    tasks.sort()
    fin = 0
    for i in range(0,len(tasks)):
        for j in range(i+1,len(tasks)):
            if tasks[j] != tasks[i]:
                break
        n = j-i-1
        print(n,tasks[i],tasks[j])
        if n%3 == 0:
            fin += n/3
        elif n > 2:
            fin += fun(n)
        elif n == 2:
            fin += 1
        elif n < 2 :
            return -1
    return fin

"""    amount = []
    fin = 0
    for i in r:
        amount.append(tasks.count(i))
    print(amount)
    for l in amount:
        if l < 2:
            return -1
        elif l%3 == 0:
            fin += l/3
        elif l > 2:
            fin += fun(l)
        elif l == 2:
            fin += 1
    return int(fin)
"""
def fun(n):
    numb = int(n/3)
    for i in range(numb,-1,-1):
        if (n-i*3) %2 == 0:
            return i + (n-i*3)/2


        

print(minimumRounds(5,[2,2,3,3,2,4,4,4,4,4]))