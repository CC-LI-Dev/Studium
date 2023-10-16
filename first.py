wort = input("3er Zeichenkette:")
wort2=wort
print(wort2)
for i in range(2, 8):
    if i % 2 == 0:
        wort2 = wort[2] + wort2 + wort[0]
    else:
        wort2 = wort[0] + wort2 + wort[2]
    print(wort2)