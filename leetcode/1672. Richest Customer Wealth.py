#1672. Richest Customer Wealth
def maximumWealth(self, accounts: list[list[int]]) -> int:
    for i in range(0,len(accounts)):
        k = accounts[i]
        accounts[i] = sum(k)
    return max(accounts)

print(maximumWealth(5,[[2,8,7],[7,1,3],[1,9,5]]))