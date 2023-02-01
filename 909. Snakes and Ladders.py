#909. Snakes and Ladders
def snakesAndLadders(self, board: list[list[int]]) -> int:
    tempBoard = []
    i = len(board)**2
    for x in board:
        temp = []
        for y in x:
            temp.append([y,i])
            i-=1
        tempBoard.append(temp)

    for l in range(len(tempBoard)):
        for k in range(len(tempBoard)):
            if tempBoard[l][k][0] == -1:
                tempBoard[l][k] = 0
            else:
                tempBoard[l][k] = tempBoard[l][k][0] - tempBoard[l][k][1]
    for x in tempBoard:
        print(x) 
print(snakesAndLadders(5,[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))