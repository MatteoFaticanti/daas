from collections import defaultdict
import numpy as np
from sympy import false, true
import environment as env
import time

def selection():
    # Nested dictionary that maps state ->(action -> action-value)
    Q = defaultdict(lambda: np.zeros(len(env.action_space)))
    s_0 = env.reset()
    while True:
        mission = np.random.choice(env.missions)
        if check_free(s_0):
            s_0 = free_drones(s_0)
        new_state,drones = choose_drones(mission, Q, s_0)
        s_0 = new_state

def choose_drones(mission, Q: defaultdict, s_0: frozenset, gamma:float=0.99, eps:float=0.05, lr:float=0.01): 
    print(s_0)
    # selected action according to policy
    action = egreedy_policy(Q, s_0, eps)
    # take selected action and go to next state getting a reward
    s_1, reward = env.step(set(s_0), action, mission)
    best_next = np.argmax(Q[s_1])
    # update state-action value using Bellman Equation  
    Q[s_0][action] += lr*(reward + gamma*best_next - Q[s_0][action])
    drones = env.action_space[action]
    return s_1, drones


def egreedy_policy(Q: defaultdict, state: frozenset, epsilon: float):
    # Epsilon greedy policy function
    return (
        # chose random action epsilon times
        np.random.choice(np.arange(len(env.action_space) - 1))
        # chose action action with max value 1 - epsilon times
        if np.random.rand() < epsilon
        else np.argmax(Q[state])
    )

def check_free(state):
    s = env.free_drones.copy()
    for i in state:
        s = s - i[0]
    if not s:
        return true
    return false

def free_drones(state):
    s = set(state.copy())
    # for every set of drones in the state check if the mission is finished
    for i in state:
        # check if difference between current time and timestep is greater 
        # then the calculated completion time for that mission (5 is a placeholder)
        if time.time() - i[1].time >= 5:
            # if mission completed remove the couple drones,mission from state
            s.remove(i)
    return frozenset(s)

print(selection())
