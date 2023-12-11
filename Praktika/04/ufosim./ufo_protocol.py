import matplotlib.pyplot as plt # type: ignore
import math

global protocol 
protocol: list = [] #(30,45),(-115,-170),(-10,200),(29,-39),(-59,59)

def add_to_protocol(p: tuple) -> None:
    protocol.append(p)
    # list = [(3,3),(-1,-1),(-1,2),(2,-3),(5,5)]
def bbox(points: list, step:int) -> tuple:
    float(step)
    if points == [] or step < 1:
        return (0.0,0.0,0.0,0.0)
    sorted_points_x = sorted(points)
    min_x = sorted_points_x[0][0]
    max_x = sorted_points_x[-1][0]
    sorted_points_y = sorted(points, key=lambda a: a[1])
    min_y = sorted_points_y[0][1]
    max_y = sorted_points_y[-1][1]
    if min_x % step != 0: 
        new_val = 0
        while new_val < abs(math.floor((min_x))):
            new_val = new_val + step
        if min_x < 0:
            new_val = new_val*(-1)
        min_x = new_val
    if max_x % step != 0:
        new_val = 0
        while new_val < abs(max_x):
            new_val = new_val + step
        if max_x < 0:
            new_val = new_val*(-1)
        max_x = new_val
    if min_y % step != 0:
        new_val = 0
        while new_val < abs(min_y):
            new_val = new_val + step
        if min_y < 0:
            new_val = new_val*(-1)
        min_y = new_val
    if max_y % step != 0:
        new_val = 0
        while new_val < abs(max_y):
            new_val = new_val + step
        if max_y < 0:
            new_val = new_val*(-1)
        max_y = new_val

    return ((min_x,max_x,min_y,max_y))
    
def plot_protocol() -> None:
    print(protocol)
    plt.title("UFO")
    plt.xlabel("x")
    plt.ylabel("y")
    protocol.insert(0,(0.0,0.0))
    coordin = bbox(protocol,10)
    #protocol.pop(0)
    x_list: list = []
    y_list: list = []
    print(coordin)
    for i in range(coordin[0],coordin[1],10):
        x_list.append(i)
    for i in range(coordin[2],coordin[3],10):
        y_list.append(i)

    plt.hlines(y_list, coordin[0], coordin[1], "lightgray", ":")
    plt.vlines(x_list, coordin[2], coordin[3], "lightgray", ":")
    plt.plot([0], [0],"o", color="black")
    print([x[0] for x in protocol],[y[1] for y in protocol] )
    plt.plot([x[0] for x in protocol],[y[1] for y in protocol] )
    plt.show()

#plot_protocol()