class AttackValidator:
    def can_attack(self, unit_type: UnitType, src: Location, target: Location) -> bool:

        # violates OCP
        if unit_type == UnitType.SOLDIER:
            return self.are_adjacent(src, target)
        elif unit_type == UnitType.FENCER:
            ...
        elif unit_type == UnitType.NEW_UNIT_TYPE:
            ...
        else:
            ...
