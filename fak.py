def fak(n=1):
    fak_val = 2
    for i in range(1,n-1):
        fak_val = fak_val*(i+2)
    if n == 0 or n == 1:
        return 1
    return fak_val

print(fak(4))