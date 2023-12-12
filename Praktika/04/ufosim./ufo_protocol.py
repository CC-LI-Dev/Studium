import matplotlib.pyplot as plt # type: ignore

global protocol 
protocol: list = [] 

def add_to_protocol(p: tuple) -> None:
    protocol.append(p)
    
def bbox(points: list, step:int) -> tuple:
    float(step)
    if points == [] or step < 1:
        return (0.0,0.0,0.0,0.0)
    sorted_points_x = sorted(points)
    min_x = sorted_points_x[0][0]
    max_x = sorted_points_x[-1][0]
    sorted_points_y = sorted(points, key=lambda a: a[1]) # sortiert anhand des 2. Indizes (hier die y Werte)
    min_y = sorted_points_y[0][1]
    max_y = sorted_points_y[-1][1]
    
    if min_x % step != 0: 
        new_val = 0
        new_val = min_x // step
        new_val = new_val*step
        min_x = new_val
    if max_x % step != 0:
        new_val = 0
        new_val = max_x // step + 1
        new_val = new_val*step
        max_x = new_val
    if min_y % step != 0:
        new_val = 0
        new_val = min_y // step
        new_val = new_val*step
        min_y = new_val
    if max_y % step != 0:
        new_val = 0
        new_val = max_y // step + 1
        new_val = new_val*step
        max_y = new_val

    return ((min_x,max_x,min_y,max_y))
    
def plot_protocol() -> None:
    
    plt.title("UFO")
    plt.xlabel("x Werte")
    plt.ylabel("y Werte")
    protocol.insert(0,(0.0,0.0))
    coordin = bbox(protocol,10)
    
    x_list: list = []
    y_list: list = []
    
    for i in range(int(coordin[0]),int(coordin[1])+1,10):
        x_list.append(i)
    for i in range(int(coordin[2]),int(coordin[3])+1,10):
        y_list.append(i)

    plt.hlines(y_list, coordin[0], coordin[1], "lightgray", ":")
    plt.vlines(x_list, coordin[2], coordin[3], "lightgray", ":")
    plt.plot([0], [0],"o", color="black")
    
    plt.plot([x[0] for x in protocol],[y[1] for y in protocol] )
    plt.show()
