st = 'sdsffffse'

'''
def long_repeat(inp):
    res = {}
    for i in inp:
        res[i] = (inp.count(i))
    print(res)
    print(max(res.values()))
    return max(res.values())
'''
def long_repeat(inp):
    count = 1
    res = []
    if len(inp) == 0:
        return 0
    else:
        for i in range(0, len(inp)-1):
            if inp[i] == inp[i+1]:
                count += 1
                #res.append(count)
            else:
                count = 1
            res.append(count)

    print(res)
    print(max(res))
    return max(res)

long_repeat(st)





