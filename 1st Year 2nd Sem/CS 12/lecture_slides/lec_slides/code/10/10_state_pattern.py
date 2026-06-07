from __future__ import annotations
import time
from abc import abstractmethod, ABC
 

class TrafficLight:
    def __init__(self):
        self._state = GoState(self)
 
    def change_state(self, state: TrafficLightState):
        self._state = state
 
    def next(self):
        self._state.next()
 
    def get_light_color(self):
        return self._state.get_light_color()


class TrafficLightState(ABC):
    def __init__(self, traffic_light: TrafficLight):
        self._traffic_light = traffic_light
 
    def set_state(self, state: TrafficLightState):
        self._traffic_light.change_state(state)
 
    @abstractmethod
    def next(self): ...
 
    @abstractmethod
    def get_light_color(self) -> str: ...



class GoState(TrafficLightState):
    def next(self):
        # _ variables are not truly private; children
        # can access them (i.e., "protected")
        self.set_state(CautionState(self._traffic_light))
 
    def get_light_color(self) -> str:
        return "green"


class CautionState(TrafficLightState):
    def next(self):
        self.set_state(StopState(self._traffic_light))
 
    def get_light_color(self) -> str:
        return "amber"


class StopState(TrafficLightState):
    def next(self):
        self.set_state(GoState(self._traffic_light))
 
    def get_light_color(self) -> str:
        return "red"
traffic_light = TrafficLight()


while True:
    print(traffic_light.get_light_color())
    traffic_light.next()
    time.sleep(1)