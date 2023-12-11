from ufosim3_2_8q import UfoSim
from ufo_autopilot import flight_distance_mult
from ufo_autopilot import fly_to
from ufo_routing import fac
from ufo_routing import find_shortest_route
from ufo_protocol import plot_protocol
#from operator import itemgetter

# Hier Konsoleingabe des Ziels x, y und der Flughoehe z ergaenzen
n_dest = int(input("Wieviele Ziele sollen angeflogen werden?"))
destinations = []
#for i in range(0,n_dest):
#    x = float(input("Zu welcher X Koordinate soll geflogen werden?"))
 #   y = float(input("Zu welcher Y Koordinate soll geflogen werden?"))
  #  p = (x,y)
   # destinations.append(p)
z = float(input("Bei welcher Höhe Z soll geflogen werden?"))
print("Die Anzahl möglicher Routen beträgt:"+str(fac(n_dest)))
destinations = [(55.0, 20.0), (-116.5, 95.0),(-10.0, -40.0), (-115.0, 95.0)]
destinations = find_shortest_route(destinations)
#destinations.sort(key=itemgetter(0))

# Die Simulation wird erstellt und gestartet.
sim = UfoSim()
speedup = 10
scaling = 2
sim.start(speedup, scaling, destinations)

# Hier Konsolausgabe der zu fliegenden Distanz ergaenzen
print(flight_distance_mult(destinations, z))

# Fliege das Ufo zum Ziel
for j in range(0,n_dest):
    fly_to(sim, destinations[j], z)
fly_to(sim,(0.0,0.0),z)
# Hier Konsolausgabe der tatsaechlich geflogenen Distanz ergaenzen
print(sim.get_dist())

plot_protocol()

# Terminiere die Simulation
sim.terminate()
