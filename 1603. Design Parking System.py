#2114. Maximum Number of Words Found in Sentences
def mostWordsFound(self, sentences: list[str]) -> int:
    count = 0
    for i in sentences:
        x = i.count(" ")
        if x > count :
            count = x
    return count+1

print(mostWordsFound(5,["please wait", "continue to fight", "continue to win"]))