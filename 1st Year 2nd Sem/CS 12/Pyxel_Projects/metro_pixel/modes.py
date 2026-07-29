from dataclasses import dataclass
from constants import GameMode

@dataclass(frozen=True)
class ModeConfig:
    mode: GameMode
    name : str
    max_days : int | None
    day_phase_sec : int
    night_phase_sec : int
    starting_money : int
    money_per_day : int

    @property
    def day_length_sec(self):
        return self.day_phase_sec + self.night_phase_sec


MODE_REGISTRY : dict[GameMode, ModeConfig] = {
    GameMode.CLASSIC : ModeConfig(
        mode = GameMode.CLASSIC,
        name = "Classic",
        max_days= 10,
        day_phase_sec= 60,
        night_phase_sec= 60,
        starting_money= 500,
        money_per_day= 300,
    ),

    GameMode.ENDLESS : ModeConfig(
        mode = GameMode.ENDLESS,
        name = "Endless",
        max_days= None,
        day_phase_sec= 60,
        night_phase_sec= 60,
        starting_money= 500,
        money_per_day= 300,
    )



}