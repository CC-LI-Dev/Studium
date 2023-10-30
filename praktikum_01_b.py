from math import *
x1 = 0
y1 = 0
x2 = 0
y2 = 0
i = 0

# Input Schleife mit Fehlerfilter
while x1 <= 0 or y1 <= 0 or x2 <= 0 or y2 <= 0 or x2 < x1 or x2 < x1:
    x1 = float(input("Punkt x1:"))
    y1 = float(input("Punkt y1:"))
    x2 = float(input("Punkt x2:"))
    y2 = float(input("Punkt y2:"))
    if i > 0:
        print("Mindestens eine der Eingaben ist Fehlerhaft.")
        print("Anforderungen: 1. Alle Werte >= 0 und 2. x2>=x1 y2>=y1")
    i = i+1
# Berechnung der Katheten
line_x1_to_x2 = x2-x1
line_y1_to_y2 = y2-y1

# Entscheidung über Art des Winkels (90 Grad, kein Winkel, normale Berechnung)
if line_x1_to_x2 == 0 and line_y1_to_y2 != 0:
    phi = pi/2
    
elif line_x1_to_x2 == 0 and line_y1_to_y2 == 0:
    phi = False
else:
    angle_tan = line_y1_to_y2/line_x1_to_x2
    phi = atan(angle_tan)

# Output
if phi == False:
    print("Identische Punkte. Es liegt kein Winkel dazwischen")
else:
    print(degrees(phi))
