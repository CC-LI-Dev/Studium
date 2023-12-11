import itertools
from ufo_autopilot import flight_distance_mult

def fac(m: int = 1, n: int = 1) -> int:
    if m < n:
        return 1
    elif m == n:
        return n
    else:
        return n*fac(m-1,n+1)*m
    
def find_shortest_route(destinations:list) -> list:
    
    routes_as_tuple = list(itertools.permutations(destinations))
    routes: list[list] = []
    shortest_route: list[list] = []
    
    for i, route in enumerate(routes_as_tuple):
        routes.insert(0,list(route))

    shortest_route_val = flight_distance_mult(routes[0],0.0)
    shortest_route = routes[0]
    
    for j in routes:
        current_route = flight_distance_mult(j,0.0)
        if current_route <= shortest_route_val:
            shortest_route_val = current_route
            shortest_route = j
    
    return shortest_route