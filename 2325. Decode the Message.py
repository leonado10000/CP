#2325. Decode the Message
def decodeMessage(self, key: str, message: str) -> str:
    wrd = []
    for i in key:
        if (i not in wrd) and (i != " "):
            wrd.append(i)
    ans = ""
    for i in message:
        if i == " ":
            ans += " "
        else:
            p = wrd.index(i)
            x = chr(97+p)
            ans += x
    return ans
print(decodeMessage(5,"the quick brown fox jumps over the lazy dog","vkbs bs t suepuv"))