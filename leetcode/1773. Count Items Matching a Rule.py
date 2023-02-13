#1773. Count Items Matching a Rule

def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    if ruleKey == "type":
            x = 0
    elif ruleKey == "color":
        x = 1
    else:
        x = 2
    c = 0
    for i in items:
        if i[x] == ruleValue:
             c+=1
    return c

print(countMatches(5,items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))