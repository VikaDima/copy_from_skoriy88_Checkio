lst = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}

def safe_pawns(inp):
    new = {(ord(i[0]), int(i[1])) for i in inp}
    safe = sum(1 for pawn in new if(pawn[0]-1, pawn[1]-1) in new or (pawn[0]+1, pawn[1]-1) in new)
    #print(safe)
    return safe

safe_pawns(lst)
'''
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('d'))
print(ord('e'))
print(ord('f'))
print(ord('g'))
print(ord('h'))
'''