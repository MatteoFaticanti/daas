from sympy import false, true
import env_classes
import geopy.distance
import itertools


depot_location = [30,37]
d1 = env_classes.Drone(500, 500, ["camera"], 500)
d2 = env_classes.Drone(500, 500, ["camera"], 500)
d3 = env_classes.Drone(500, 500, ["camera"], 500)
d4 = env_classes.Drone(500, 500, ["camera"], 500)
d5 = env_classes.Drone(500, 500, ["camera"], 500)
free_drones = {d1,d2,d3,d4,d5}
p1 = env_classes.Provider("p1", [d1], {'place1': [36.6509378, 37.1038871],'place2': [-1.444471, -1.163332],})
sl1 = env_classes.SLA(None, 280000, 5)
m1 = env_classes.Service_request({'place1': [36.6509378, 37.1038871],'place2': [-1.444471, -1.163332],}, 400, sl1, False)
m2 = env_classes.Service_request({'place1': [36.6509378, 37.1038871],'place2': [-1.444471, -1.163332],}, 400, sl1, False)
m3 = env_classes.Service_request({'place1': [36.6509378, 37.1038871],'place2': [-1.444471, -1.163332],}, 400, sl1, False)
missions = [m1, m2, m3]

def step(state, action, mission):
    #check if the choosen drones are valid, if not remain into current state and get 0 reward
    if not check_drones(state, set(action_space[action])):
        return frozenset(state), 0
    #resulting state performing a valid action
    state.add((frozenset(action_space[action]),mission))
    disposed = frozenset(state)
    #reward calculated for a valid action
    R = sl1.max_time / extimated_completion()
    return disposed, R

def check_drones(state, action):
    # check if the chosen drones are already in use
    return next(
        (false for s in state if len(s[0].intersection(action)) != 0), true
    )

def reset():
    #initial state is an empty set
    return frozenset()

def get_distance(c1):
    d = 0
    for value in p1.charging_locations.values():
        d += int(geopy.distance.distance(c1, value).m)
        c1 = value
    return d

def extimated_completion():
    s = get_distance(depot_location)
    v = 35
    return s/v

action_space = sum(
        (
            list(map(set, itertools.combinations(free_drones, i)))
            for i in range(len(free_drones) + 1)
        ),
        [],
    )