def mysort(mylist: list) -> None:
    for i in range(0,len(mylist)):
        min_ind = i
        for j in range(i,len(mylist)):
            if mylist[j] < mylist[min_ind]:
                min_ind = j
        mylist[min_ind], mylist[i] = mylist[i],mylist[min_ind]
          
mylist = [5,7,6,-10,0,77,21,23,78,-1]
mysort(mylist)
print(mylist)