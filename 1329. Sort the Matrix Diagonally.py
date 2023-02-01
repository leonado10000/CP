#1329. Sort the Matrix Diagonally
def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
    temp = []
    for i in range(len(mat)):
        for a in range(len(mat[0])):
            print(mat[i][a])
            

print(diagonalSort(5,[[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
