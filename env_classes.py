import datetime
import time

class Drone:
    def __init__(self, flight_range: float, memory_capacity: float, available_sensors: list[str], battery_lifetime: int):
        self.flight_range = flight_range            # max flight range, expressed in chilometers
        self.memory_capacity = memory_capacity      # memory capacity, expressed in GB
        self.available_sensors = available_sensors  # available sensors, example: ["camera", "microphone", "bluetooth"]
        self.battery_lifetime = battery_lifetime    # remaining battery life, expressed in mAH

class SLA:
    def __init__(self, mission_start_time: datetime, max_time: int, min_drones: int):
        self.mission_start_time = mission_start_time # mission starting time
        self.max_time = max_time # maximum time to complete the mission
        self.min_drones = min_drones # minimum number of drones to dispatch

class Service_request:
    def __init__(self, locations: dict[str, list[int]], resources: float, SLA: SLA, is_premium: bool, time = time.time() ):
        self.is_premium = is_premium    # True if the request is a premium one
        self.locations = locations      # locations to be visited respecting the order, example: 
                                        # {'place1': [36.6509378, 37.1038871], 
                                        # 'place2': [-1.444471, -1.163332],}
        self.resources = resources      # resources needed, expressed in GB
        self.SLA = SLA
        self.time = time

class Provider:
    def __init__(self, name: str, drones: list[Drone], charging_locations: dict[str, list[int]]):
        self.drones = drones
        self.charging_locations = charging_locations
