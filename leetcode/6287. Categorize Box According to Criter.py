#6287. Categorize Box According to Criteria
def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
    if length >= 10000 or width >= 10000 or height >= 1000 or height*length*width >= 1000000000:
        if mass >= 100:
            return "Both"
        else:
            return "Bulky"
    else:
        if mass >= 100:
            return "Heavy"
        else:
            return "Neither"