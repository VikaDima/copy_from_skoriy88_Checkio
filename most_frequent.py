inp = [ 'a', 'bi', 'bi', 'bi', 'a']
print(inp.sort())
def most_frequent(lst):
    res = [(lst.count(i), i) for i in lst]

    #print(max(res)[1])
    return max(res)[1]

most_frequent(inp)