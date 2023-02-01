#1859. Sorting the Sentence
def sortSentence(self, s: str) -> str:
    c = 1
    s = s.split(" ")
    fin = []
    for i in s:
        try: 
            int(i[-1])
            if int(i[-1])>c:
                c = int(i[-1])
        except ValueError:
            continue
    for i in range(c):
        fin.append("")

    for i in s:
        fin[int(i[-1])-1] = i[:len(i)-1]
    re = ""
    for x in fin:
        re += x + " "
    return re[:-1]

print(sortSentence(5,"is2 sentence4 This1 a3"))