#Annäherung cos(x)

from math import *

#Eingabe und Variablen Definition
x = float(input("X:"))
n = int(input("Näherungsparameter:"))
approx_value = 1
x_standin = x*x
fak = 2

#Berechnung Annäherung
for i in range(1,n):
    # Vorzeichenwechsel
    if i % 2 != 0:
        k = -1
    # Berechnung
    approx_value = approx_value + k*((1)/(fak))*x_standin
    # neue Fakultätswerte, höheres Exponential und Reset des Vorzeichens
    fak = fak*(2*i+1)*(2*i+2)  
    x_standin = x_standin*x*x
    k = 1

# Output
print(approx_value)
# print(cos(x))
error_value = abs(cos(x)-approx_value)
print("Fehler:"+str(error_value))
