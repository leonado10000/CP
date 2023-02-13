#32. Longest Valid Parentheses
def longestValidParentheses(self, s: str) -> int:
    maz1 = [0,0]
    maz2 = [0,0]
    i = 0 
    start , end = 0,0

    #get a starting point for substring
    while(i<len(s)):
        #all subtring start with "("
        if s[i] == "(":
            flag = 0 #flag to change if substring invalid to stop further process
            start = i
            for j in range(i+2,len(s),2):
                #print(j,i)
                if not isvalid(s[i:j+1]) :
                    flag = 1
                    end = j
                    

            # if flag doesnt change it means
            # till last i.e. j subtring is continuesly valid hence 
            if flag == 0 :
                start = i
                end = j+1
                i = end
            
            # check and process values for start and end of subtring
            if end-start > maz2[1]- maz2[0]:
                maz2[0] = start
                maz2[1] = end

        if maz1[1] == maz2[0]:
            maz1[1] = maz2[1]
        elif maz1[1]-maz1[0] < maz2[1]-maz2[0]:
            maz1[0] = maz2[0]
            maz1[1] = maz2[0]
        i+=1
    return maz1[1]-maz1[0]

#checking valid substring
def isvalid(string):
    open = 0
    for i in string:
        if i == "(" :
            open += 1
        elif i == ")" :
            if open < 1 :
                return False
            open -= 1
    if open != 0:
        return False
    else:
        return True
print(longestValidParentheses(5,"()()"))