words = []

with open("Studium-1/DerWerwolf.txt","r") as fh:
    for line in fh:
        words.extend(line.rstrip().split(" "))
#words.sort(key=len)
print(words)