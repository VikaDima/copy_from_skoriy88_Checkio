st = [1, 1, 1, 1, 1, 1]

def all_the_same(inp):
    res = True
    if len(inp) == 0 or len(inp) == 1:
        return res
    else:
        for i in range(0, len(inp)-1):
            if inp[i+1] == inp[i]:
                res = True
            else:
                res = False
                break
    print(res)
    return res

all_the_same(st)