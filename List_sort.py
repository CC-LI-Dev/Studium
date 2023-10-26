x = []
n = int(input("Wieviele Zahlen wollen Sie vergleichen?"))
for i in range(0,n):
    list_in = input("Geben Sie eine Zahl an:")
    x.append(list_in)
newlist=[]
while x:
    min_var = x[0]  
    for i in x: 
        if i < min_var:
            min_var = i
    newlist.append(min_var)
    x.remove(min_var)    

print(newlist[-1])