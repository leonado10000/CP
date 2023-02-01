#1678. Goal Parser Interpretation
def interpret(self, command: str) -> str:
    sol = ""
    for i in range(0,len(command)) :
        if command[i] == "(":
            if command[i+1] == ")" :
                sol += "o"
            else :
                sol += "al"
        elif command[i] == "G" :
            sol += "G"
    return sol

print(interpret(5,"G()()()()(al)"))