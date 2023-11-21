import time
import math

def fly_to(sim, x: float, y: float, z: float) -> None:
    takeoff(sim, z)
    cruise(sim, x, y)
    landing(sim)

def takeoff(sim, z: float) -> None:
    # Das Ufo fliegt senkrecht nach oben mit 10 km/h.
    sim.set_i(90)
    sim.request_delta_v(10)

    # Rechtzeitig vor dem Erreichen der Zielhoehe, bremst das Ufo auf 1 km/h.
    while sim.get_z() < z - 2:
        time.sleep(0.05)
    sim.request_delta_v(-9)

    # Wenn das Ufo ganz nahe dran ist, stoppt es und richtet sich horizontal aus.
    while sim.get_z() < z - 0.05:
        time.sleep(0.05)
    sim.request_delta_v(-1)
    sim.set_i(0)

def cruise(sim, x: float, y: float) -> None:
    # Das Ufo ist in der aktuellen Position gestartet.
    fro_x = sim.get_x()
    fro_y = sim.get_y()

    # Weiter geht es in Richtung Ziel. Die zu fliegende Distanz ist dist.
    sim.set_d(int(angle(fro_x, fro_y, x, y)))
    dist = sim.get_dist() + distance(fro_x, fro_y, x, y)

    # Das Ufo beschleunigt auf 15 km/h.
    sim.request_delta_v(15)

    # Wenn der Abstand zum Ziel 4m ist, bremst das Ufo auf 1 km/h.
    while dist - sim.get_dist() > 4:
        time.sleep(0.05)
    sim.request_delta_v(-14)

    # Wenn der Abstand zum Ziel 0.05m ist, stoppt das Ufo.
    while dist - sim.get_dist() > 0.05:
        time.sleep(0.05)
    sim.request_delta_v(-1)

def landing(sim) -> None:
    # Das Ufo fliegt senkrecht nach unten mit 10 km/h.
    sim.set_i(-90)
    sim.request_delta_v(10)

    # Wenn die Hoehe 3m erreicht, bremst das Ufo auf 1 km/h.
    while sim.get_z() > 3:
        time.sleep(0.05)
    sim.request_delta_v(-9)

    # Das Ufo ist gelandet, wenn die Hoehe kleiner gleich 0 ist.
    while sim.get_z() > 0:
        time.sleep(0.05)
def distance(x1: float, y1: float, x2: float, y2: float, z: float):
    dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return dist
    