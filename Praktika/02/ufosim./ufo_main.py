from ufosim3_2_8q import UfoSim
from ufo_autopilot import flight_distance
from ufo_autopilot import fly_to

# Hier Konsoleingabe des Ziels x, y und der Flughoehe z ergaenzen
x = float(input("Zu welcher X Koordinate soll geflogen werden?"))
y = float(input("Zu welcher Y Koordinate soll geflogen werden?"))
z = float(input("Bei welcher Höhe Z soll geflogen werden?"))

# Die Simulation wird erstellt und gestartet.
sim = UfoSim()
speedup = 5
scaling = 10
destinations = [(x, y)]
sim.start(speedup, scaling, destinations)

# Hier Konsolausgabe der zu fliegenden Distanz ergaenzen

# Fliege das Ufo zum Ziel
fly_to(sim, x, y, z)

# Hier Konsolausgabe der tatsaechlich geflogenen Distanz ergaenzen

# Terminiere die Simulation
sim.terminate()
