def isprefix(beg: str, end: str) -> bool:
    len_beg = len(beg)
    if beg != end[:len_beg]:
        return False
    return True



    #if beg == end[:len_beg]:
    #    return True
    #if beg == "":
    #    return True
    
    #return False

print(isprefix("Oster","Osterhase"))
print(isprefix("Ostern","Osterhase"))
print(isprefix("Osterhasen","Osterhase"))
print(isprefix("","Osterhase"))

def isprefix_vorl(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    for i, letter in enumerate(s):
        if letter != t[i]:
            return False
    return True
        
print(isprefix_vorl("Oster","Osterhase"))
print(isprefix_vorl("Ostern","Osterhase"))
print(isprefix_vorl("Osterhasen","Osterhase"))
print(isprefix_vorl("","Osterhase"))
