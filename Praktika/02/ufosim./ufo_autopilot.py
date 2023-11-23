import time
import math

def takeoff(sim, z: float) -> None:
    # Das Ufo fliegt senkrecht nach oben mit 10 km/h.
    print(format_flight_data(sim))
    sim.set_i(90)
    sim.request_delta_v(10)

    # Rechtzeitig vor dem Erreichen der Zielhoehe, bremst das Ufo auf 1 km/h.
    while sim.get_z() < z - 2:
        time.sleep(0.05)
        print(format_flight_data(sim))
    sim.request_delta_v(-9)

    # Wenn das Ufo ganz nahe dran ist, stoppt es und richtet sich horizontal aus.
    while sim.get_z() < z - 0.05:
        time.sleep(0.05)
        print(format_flight_data(sim))
    sim.request_delta_v(-1)
    sim.set_i(0)

def cruise(sim, x: float, y: float) -> None:
    # Das Ufo ist in der aktuellen Position gestartet.
    fro_x = sim.get_x()
    fro_y = sim.get_y()
    print(format_flight_data(sim))

    # Weiter geht es in Richtung Ziel. Die zu fliegende Distanz ist dist.
    sim.set_d(int(angle(fro_x, fro_y, x, y)))
    dist = sim.get_dist() + distance(fro_x, fro_y, x, y)

    # Das Ufo beschleunigt auf 15 km/h.
    sim.request_delta_v(15)


    # Wenn der Abstand zum Ziel 4m ist, bremst das Ufo auf 1 km/h.
    while dist - sim.get_dist() > 4:
        time.sleep(0.05)
        print(format_flight_data(sim))
    sim.request_delta_v(-14)

    # Wenn der Abstand zum Ziel 0.05m ist, stoppt das Ufo.
    while dist - sim.get_dist() > 0.05:
        time.sleep(0.05)
        print(format_flight_data(sim))
    sim.request_delta_v(-1)

def landing(sim) -> None:
    # Das Ufo fliegt senkrecht nach unten mit 10 km/h.
    sim.set_i(-90)
    sim.request_delta_v(10)
    print(format_flight_data(sim))

    # Wenn die Hoehe 3m erreicht, bremst das Ufo auf 1 km/h.
    while sim.get_z() > 3:
        time.sleep(0.05)
        print(format_flight_data(sim))
    sim.request_delta_v(-9)

    # Das Ufo ist gelandet, wenn die Hoehe kleiner gleich 0 ist.
    while sim.get_z() > 0:
        time.sleep(0.05)
        print(format_flight_data(sim))
    
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return dist

def angle(x1: float, y1: float, x2: float, y2: float) -> float:
    vect_x2 = x2-x1
    vect_y2 = y2-y1
    vect_y1 = 0
    vect_x1 = x1 + 1

    if vect_x2 == 0 and vect_y2 == 0:
        return 0

    gamma = (vect_x1*vect_x2+vect_y1*vect_y2)/((math.sqrt((vect_x1**2)+(vect_y1**2)))*math.sqrt((vect_x2**2)+(vect_y2**2)))
    angle_val = math.degrees(math.acos(gamma))
    
    if angle_val == 0:
        return 0
    elif y2 < y1:
        return 360-angle_val
    else:
        return angle_val
    
def flight_distance(x1: float, y1: float, x2: float, y2: float, z: float) -> float:
    flight_dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2)) + 2*z
    return flight_dist

def format_flight_data(sim) -> str:
    return str(sim.get_ftime())+"s:"+str(sim.get_x())+" "+str(sim.get_y())+" "+str(sim.get_z())

def fly_to(sim, x: float, y: float, z: float) -> None:
    takeoff(sim, z)
    cruise(sim, x, y)
    landing(sim)

def fac(m: int = 1, n: int = 1) -> int:
    if m < n:
        return 1
    elif m == n:
        return n*fac(m-1,n+1)
    else:
        return n*fac(m-1,n+1)*m
    