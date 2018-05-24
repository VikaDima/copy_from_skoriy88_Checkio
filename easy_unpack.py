tup = (1, 2, 3, 4, 5, 6, 7, 9)
print(type(tup))
def easy_unpack(inp):
    inp = tuple(inp)
    res = (inp[0], inp[2], inp[-2])
    #print(res)
    return res

easy_unpack(tup)