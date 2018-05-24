'''
0 < text < 50
-26 < delta < 26
'''
inp = "simple text"
alpha = 'abcdefghijklmnopqrstuvwxyz'

def to_encrypt(text, delta):
    res = []
    for i in range(0, len(text)):
        if text[i] == ' ':
            res.append(' ')
        else:
            if 0 <= alpha.find(text[i]) + delta <=  len(alpha) - 1:
                res.append(alpha[alpha.find(text[i]) + delta])
            elif alpha.find(text[i]) + delta > len(alpha) -1:
                res.append(alpha[alpha.find(text[i]) + delta - len(alpha)])
            else:
               res.append(alpha[alpha.find(text[i]) + delta + len(alpha)])
    res = ''.join(res)
    print(res)
    return res

to_encrypt(inp, 16)
to_encrypt("a b c", -3)

def to_encrypt(text, delta):
    return ''.join([chr(ord('a') + (ord(i) + delta - ord('a')) % 26) if i != ' ' else ' ' for i in text ])

def to_encrypt(text, delta):
    return ''.join(chr(ord('a') + (ord(c) - ord('a') + delta) % 26)
                   if c != ' ' else ' ' for c in text)

to_encrypt=lambda t,k:''.join([x,chr(97+(ord(x)-97+k)%26)]['`'<x<'{']for x in t)

def to_encrypt(text, delta):
    f = lambda c: chr((ord(c) + 7 + delta) % 26 + 97) if c.isalpha() else c
    return ''.join(map(f, text))

