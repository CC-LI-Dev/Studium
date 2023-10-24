from math import *
x = float(input("X:"))
n = int(input("Näherungsparameter:"))
approx_value = 1
x_standin = x*x
fak = 2


for i in range(0,n):
    if i % 2 == 0:
        k = -1
    approx_value = approx_value + k*((1)/(fak))*x_standin
    fak = fak*(2*i+3)*(2*i+4)
    x_standin = x_standin*x*x
    k = 1



print(approx_value)
error_value = abs(cos(x)-approx_value)
print("Fehler:"+str(error_value))
