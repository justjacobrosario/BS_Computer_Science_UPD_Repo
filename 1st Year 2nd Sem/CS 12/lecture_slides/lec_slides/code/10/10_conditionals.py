class TrafficLightState(Enum):
    STOP = auto()
    CAUTION = auto()
    GO = auto()


class TrafficLight:
    def __init__(self, state: TrafficLightState):
        self._state = state
 
    def next(self):
        match self._state:
            case TrafficLightState.STOP:
                self._state = TrafficLightState.GO
            case TrafficLightState.GO:
                self._state = TrafficLightState.CAUTION
            case TrafficLightState.CAUTION:
                self._state = TrafficLightState.STOP
 
    def get_light_color(self):
        match self._state:
            case TrafficLightState.STOP:
                return 'red'
            case TrafficLightState.GO:
                return 'green'
            case TrafficLightState.CAUTION:
                return 'amber'