'''
0 < text < 50
-26 < delta < 26
'''
inp = "important text"
alpha = 'abcdefghijklmnopqrstuvwxyz'
print(len(alpha))

def to_encrypt(text, delta):
    res = []
    for i in range(0, len(text)-1):
        if text[i] == ' ':
            res.append(' ')
        else:
            if alpha.find(text[i]) + delta < len(alpha) - 1:
                print(alpha[alpha.find(text[i]) + delta])
                res.append(alpha[alpha.find(text[i]) + delta])
    print(res)
    return res

to_encrypt(inp, 3)