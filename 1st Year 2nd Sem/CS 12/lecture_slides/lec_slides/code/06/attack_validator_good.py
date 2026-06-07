class AttackValidator(Protocol):
    # Notice that `unit_type: UnitType` is not a parameter anymore
    def can_attack(self, src: Location, target: Location) -> bool:
        ...
 
 
class SoldierAttackValidator:  # SoldierAttackValidator <: AttackValidator
    def can_attack(self, src: Location, target: Location) -> bool:
        return src.manhattan(target) == 1
 
 
class ArcherAttackValidator:  # ArcherAttackValidator <: AttackValidator
    def can_attack(self, src: Location, target: Location) -> bool:
        return 1 <= src.manhattan(target) <= 5
 
 
class FencerAttackValidator:  # FencerAttackValidator <: AttackValidator
    def can_attack(self, src: Location, target: Location) -> bool:
        return src.manhattan(target) == 1 and (src.same_row(target) or src.same_col(target))
