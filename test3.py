# A nested dictionary that maps
# state -> (action -> action-value)
from collections import defaultdict
from os import remove
import numpy as np
from sympy import true
import environment as env
import env_classes

state = (((1,2,3),"m1"), ((4,5,6),"m2"))
action = (7,8)
action2 = (7)
value = 1
value2 = 9

Q = defaultdict(lambda: np.zeros(len(env.action_space)))
Q[((1,2),"m1")][2] = 2
Q[((1,2),"m2")][3] = 620

def best_action(Q):
    best_next = 0
    max = 0
    for state in Q:
        v = np.argmax(Q[state]) 
        m = np.max(Q[state]) 
        if m > max:
            best_next = v
    return best_next

#print(Q)
#print(best_action(Q))

#print(tuple({1,2}) + tuple({1}))

def check_drones(state, action):
    return state.isdisjoint(action)

#print(check_drones({1,2}, {1,3}))



from threading import Timer

l = {(1,"m1"), (2,"m2"), (3,"m1"),(1,"m3")}
to_remove = []

def hello(mission):
    for i in l:
        if i[1] == mission:
            to_remove.append(i)
    print(to_remove)


t = Timer(5.0, hello, ["m1"])
#t.start() # after 30 seconds, "hello, world" will be printed
import time
'''
def selection():
    # Nested dictionary that maps state ->(action -> action-value)
    Q = defaultdict(lambda: np.zeros(len(env.action_space)))
    s_0 = env.reset()
    while True:
        mission = np.random.choice(env.missions)
        new_state,drones = choose_drones(mission, Q, s_0)
        t = Timer(5.0, expiration, [mission, s_0])
        t.start()
        s_0 = new_state

def expiration(mission, state):
    for i in state:
        if i[1] == mission:
            to_remove.append(i)
    print(to_remove)


m = time.time()
li = [m]
while(true):
    print(time.time() - m)
    if time.time() - m >= 5:
        li.remove(m)
        break
print(li)
'''
sl1 = env_classes.SLA(None, 280000, 5)
m1 = env_classes.Service_request({'place1': [36.6509378, 37.1038871],'place2': [-1.444471, -1.163332],}, 400, sl1, False)
m2 = env_classes.Service_request({'place1': [36.6509378, 37.1038871],'place2': [-1.444471, -1.163332],}, 400, sl1, False)
m3 = env_classes.Service_request({'place1': [36.6509378, 37.1038871],'place2': [-1.444471, -1.163332],}, 400, sl1, False)
missions = [m1, m2, m3]

l = {(1,m1), (2,m2), (3,m1),(1,m3)}

def free_expired():
    s = l.copy()
    for i in l:
        if time.time() - i[1].time >= 3:
            s.remove(i)
    return s

free_drones = {1,2,3,4,5}

def check_free():
    s = set()
    for i in l:
        s = free_drones - {1,2}
    return s

print(check_free())