from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, max_health: int):
        self._health = max_health
        self._max_health = max_health

    @abstractmethod
    def can_attack(self, target: Location) -> bool:
        raise NotImplementedError

    @property
    def health(self) -> int:
        return self._health

    # ...


class Soldier(Character):
    def can_attack(self, target: Location) -> bool:
        return src.manhattan(target) == 1


base = Character(12)  # Error; abstract base class
# cannot be instantiated

soldier = Soldier(12)

print(soldier.health())
print(soldier.can_attack(...))

