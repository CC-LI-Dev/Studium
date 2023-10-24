from math import *

x1 = float(input("Punkt x1:"))
y1 = float(input("Punkt y1:"))
x2 = float(input("Punkt x2:"))
y2 = float(input("Punkt y2:"))

line_x1_to_x2 = x2-x1
line_y1_to_y2 = y2-y1
if line_x1_to_x2 == 0:
    phi = pi/2
else:
    angle_tan = line_y1_to_y2/line_x1_to_x2
    phi = atan(angle_tan)

print(degrees(phi))
