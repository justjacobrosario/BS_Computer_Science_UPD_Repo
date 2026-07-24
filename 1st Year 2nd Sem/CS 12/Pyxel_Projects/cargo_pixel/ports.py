from constants import Cargo, CARGO_GEN_MAX_SEC, CARGO_GEN_MIN_SEC, FPS
from abc import ABC
from random import choice, randint


class Port(ABC):
    def __init__(self, x, y, allowed_cargo, cargo_cap=4):
        self.x = x
        self.y = y
        self.allowed_cargo = allowed_cargo
        self.cargos_to_ship = []
        self.cargo_cap = cargo_cap
        self.ticks_until_next_cargo = randint(CARGO_GEN_MIN_SEC * FPS, CARGO_GEN_MAX_SEC * FPS)
        self.ticks_for_current_cycle = self.ticks_until_next_cargo


    def generate_cargo(self, possible_cargos: list[Cargo] = [Cargo.RED, Cargo.ORANGE, Cargo.YELLOW, Cargo.GREEN, Cargo.BLUE]):
        if len(self.cargos_to_ship) < self.cargo_cap:
            new_cargo = choice(possible_cargos)
            self.cargos_to_ship.append(new_cargo)

    def remove_cargo(self, cargo: Cargo | None = None):
        if cargo is None:
            self.cargos_to_ship.pop(0)
        elif cargo in self.cargos_to_ship:
                self.cargos_to_ship.remove(cargo)

    def upd_cargo_timer(self):
        self.ticks_until_next_cargo -= 1
        if self.ticks_until_next_cargo <= 0:
            self.generate_cargo()
            self.ticks_until_next_cargo = randint(CARGO_GEN_MIN_SEC * FPS, CARGO_GEN_MAX_SEC * FPS)
            self.ticks_for_current_cycle = self.ticks_until_next_cargo

    @property
    def progress(self):
        if self.cargo_cap <= 0:
            return 0.0
        if len(self.cargos_to_ship) >= self.cargo_cap:
            return 1.0
        
        slot_size = 1 / self.cargo_cap
        base = len(self.cargos_to_ship) * slot_size

        if self.ticks_for_current_cycle <= 0:
            cycle_fraction = 0.0
        else:
            elapsed = self.ticks_for_current_cycle - self.ticks_until_next_cargo
            cycle_fraction = elapsed / self.ticks_for_current_cycle

        cycle_fraction = max(0.0, min(1.0, cycle_fraction))

        p = base + slot_size * cycle_fraction
        return max(0.0, min(p, 1.0))

class RedPort(Port):
    def __init__(self, x, y):
        super().__init__(x, y, Cargo.RED)

class OrangePort(Port):
    def __init__(self, x, y):
        super().__init__(x, y, Cargo.ORANGE)
    
class YellowPort(Port):
    def __init__(self, x, y):
        super().__init__(x, y, Cargo.YELLOW)

class GreenPort(Port):
    def __init__(self, x, y):
        super().__init__(x, y, Cargo.GREEN)

class BluePort(Port):
    def __init__(self, x, y):
        super().__init__(x, y, Cargo.BLUE)

