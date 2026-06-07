class AttackValidator:
    def can_attack(self, unit_type: UnitType, src: Location, target: Location) -> bool:
        match unit_type:
            case UnitType.SOLDIER:
                return src.manhattan(target) == 1
            case UnitType.ARCHER:
                return 1 <= src.manhattan(target) <= 5
            case UnitType.FENCER:
                return (
                    1 <= src.manhattan(target) <= 2 and
                    (
                      src.same_row(target) or
                      src.same_col(target)
                    )