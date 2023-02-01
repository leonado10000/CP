def possibleChanges(usernames):
    # Write your code here
    print(usernames)
    for x in usernames:
        flag1 = 0
        print(x)
        for y in range(0,len(x)-1):
            print("run")
            flag2 = 0
            for z in range(y+1,len(x)):
                if ord(x[y]) > ord(x[z]):
                    print("YES")
                    flag1 = 1
                    flag2 = 1
                    break
            if flag2 == 1:
                break
    if flag1 == 0:
        print("NO")

print(possibleChanges(["hydra"]))