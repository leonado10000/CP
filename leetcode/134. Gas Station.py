#134. Gas Station
def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
    # get rid of repeat values like gas[i+1] = cost[i]
    gas2,cost2 = [],[]
    oldposs = []
    for i in range(len(gas)-1):
        if gas[i+1] != cost[i] :
            gas2.append(gas[i])
            cost2.append(cost[i])
            oldposs.append(i)
    if gas[0] != cost[-1]:
        gas2.append(gas[i])
        cost2.append(cost[i])
        oldposs.append(i)
        
    # got through each place as that place
    for i in range(len(gas2)):
        minpos = i
        tank = gas2[i]
        # start from that place to end 
        for j in range(minpos,len(gas2)):
            if gas2[j] == 0 and cost2[j] == 0:
                continue
            tank -= cost2[j]
            if tank < 0:
                tank = -1
                break
            try:
                tank += gas2[j+1]
            except IndexError:
                tank += gas2[0]
        if tank == -1:
            continue
        else:
            #start from start to that place
            for j in range(0,minpos):
                tank -= cost2[j]
                if tank < 0:
                    tank = -1
                    break
                tank += gas2[j+1]
    
            if tank == -1:
                continue
            else:
                return oldposs[minpos]
    return -1
print(canCompleteCircuit(5,[2,3,4],[3,4,3]))