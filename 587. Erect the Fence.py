#587. Erect the Fence
def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
    if len(trees) <= 3:
        return trees

    a = trees[0]
    fence = [a,a,a,a]
        
    #find four extreme points
    ftop = trees[0][1]
    fleft = trees[0][0]
    fright = trees[0][0]
    fdown = trees[0][1]
        
    for i in range(0,len(trees)):
        a = trees[i]
        #update to  reach four max boundaries
        if a[1] > ftop:
            ftop = a[1]
            fence[0] = a
                
        elif a[1] < fdown:
            fdown = a[1]
            fence[1] = a
                
        elif a[0] > fright:
            fright = a[0]
            fence[2] = a
            
        elif a[0] < fleft:
            fleft = a[0]
            fence[3] = a
    #remove fence from trees
    for i in fence:
        trees.remove(i)
    #make four straight line equations and add points on or over the line accordingly
    # line fdown[fence[1]]-fleft[fence[3]]
    # (y-y1) = (y2-y1)(x-x1)/(x2-x1)
    for i in trees:
        x1,y1,x2,y2 = fence[1][0],fence[1][1],fence[3][0],fence[3][1]
        x,y = i[0],i[1]
        if ( (y-y1) - ((y2-y1)( x - x1)/(x2-x1)) ) == 0

    fence.sort()
    return fence

print(outerTrees(5,[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))