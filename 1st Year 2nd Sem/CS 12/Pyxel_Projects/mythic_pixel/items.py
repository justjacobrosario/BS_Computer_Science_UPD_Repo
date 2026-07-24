from abc import ABC
import random


class Helmet(ABC):
    def __init__(self):
        self.probability : float = 0
        self.exp : int = 0
        self.lvl : int = 0
        self.multiplier : float = 1.0 # higher implies more exp to cover to lvl up
        self.excess_exp : int = 0
        self.defense : int = 100

    def add_exp(self, val : int):
        self.exp += val
        self.upd_lvl()

    def upd_lvl(self):
        exp_needed = int(100*self.multiplier)
        new_lvl = self.exp // exp_needed

        if new_lvl > self.lvl:
            self.lvl = new_lvl
            self.multiplier += 0.1
            self.defense = int(self.defense * (1 + (self.lvl * 0.1)))

        self.excess_exp = self.exp % exp_needed

class CopperHelmet(Helmet):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.50
        self.defense : int = 10

class IronHelmet(Helmet):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.10
        self.defense : int = 100

class GoldenHelmet(Helmet):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.05
        self.defense : int = 250

class DiamondHelmet(Helmet):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.01
        self.defense : int = 500



'''
'''



class Chestplate(ABC):
    def __init__(self):
        self.probability : float = 0
        self.exp : int = 0
        self.lvl : int = 0
        self.multiplier : float = 1.0 # higher implies more exp to cover to lvl up
        self.excess_exp : int = 0
        self.defense : int = 100

    def add_exp(self, val : int):
        self.exp += val
        self.upd_lvl()

    def upd_lvl(self):
        exp_needed = int(100*self.multiplier)
        new_lvl = self.exp // exp_needed

        if new_lvl > self.lvl:
            self.lvl = new_lvl
            self.multiplier += 0.1
            self.defense = int(self.defense * (1 + (self.lvl * 0.1)))

        self.excess_exp = self.exp % exp_needed

class CopperChestplate(Chestplate):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.50
        self.defense : int = 100

class IronChestplate(Chestplate):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.10
        self.defense : int = 250

class GoldenChestplate(Chestplate):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.05
        self.defense : int = 500

class DiamondChestplate(Chestplate):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.01
        self.defense : int = 1000

'''
'''


class Boots(ABC):
    def __init__(self):
        self.probability : float = 0
        self.exp : int = 0
        self.lvl : int = 0
        self.multiplier : float = 1.0 # higher implies more exp to cover to lvl up
        self.excess_exp : int = 0
        self.defense : int = 100

    def add_exp(self, val : int):
        self.exp += val
        self.upd_lvl()

    def upd_lvl(self):
        exp_needed = int(100*self.multiplier)
        new_lvl = self.exp // exp_needed

        if new_lvl > self.lvl:
            self.lvl = new_lvl
            self.multiplier += 0.1
            self.defense = int(self.defense * (1 + (self.lvl * 0.1)))

        self.excess_exp = self.exp % exp_needed

class CopperBoots(Boots):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.50
        self.defense : int = 10

class IronBoots(Boots):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.10
        self.defense : int = 30

class GoldenBoots(Boots):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.05
        self.defense : int = 50

class DiamondBoots(Boots):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.01
        self.defense : int = 75


'''
'''

class Weapon(ABC):
    def __init__(self):
        self.probability : float = 0
        self.exp : int = 0
        self.lvl : int = 0
        self.multiplier : float = 1.0 # higher implies more exp to cover to lvl up
        self.excess_exp : int = 0
        self.attack : int = 100
        self.attack_speed : int = 1
        self.attack_range : int = 1
        self.sustained_damage : int | None = None

    def add_exp(self, val : int):
        self.exp += val
        self.upd_lvl()

    def upd_lvl(self):
        exp_needed = int(100*self.multiplier)
        new_lvl = self.exp // exp_needed

        if new_lvl > self.lvl:
            self.lvl = new_lvl
            self.multiplier += 0.1
            self.attack = int(self.attack * (1 + (self.lvl * 0.1)))
            self.attack_speed = int(self.attack_speed * (1 + (self.lvl * 0.1)))
            self.attack_range = int(self.attack_range * (1 + (self.lvl * 0.1)))
            if self.sustained_damage != None:
                self.sustained_damage = int(self.sustained_damage * (1 + (self.lvl * 0.1)))
        self.excess_exp = self.exp % exp_needed

class Revolver(Weapon):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.10
        self.attack = 10
        self.attack_speed = 1
        self.attack_range = 5

class FireStaff(Weapon):
    def __init__(self):
        super().__init___()
        self.probability : float = 0.10
        self.attack = 10
        self.attack_speed = 1
        self.attack_range = 5
        self.sustained_damage = 2

type Item = Weapon | Helmet | Chestplate | Boots

class Chest(ABC):
    def __init__(self):
        self.cost : int = 10
        self.items_to_luck : list[Item] = []

    def get_random_item(self):
        return random.choice(self.items_to_luck, weights = [item.probability for item in self.items_to_luck])

class CommonChest(Chest):
    def __init__(self):
        super().__init___()
        self.cost = 25
        self.items_to_luck = [CopperBoots, CopperChestplate, CopperHelmet, IronBoots, IronChestplate, IronBoots, DiamondBoots, DiamondChestplate, DiamondHelmet, Revolver, FireStaff] 

class RareChest(Chest):
    def __init__(self):
        super().__init___()
        self.cost = 25
        self.items_to_luck = [IronBoots, IronChestplate, IronBoots, DiamondBoots, DiamondChestplate, DiamondHelmet, Revolver, FireStaff] 

class LegendaryChest(Chest):
    def __init__(self):
        super().__init___()
        self.cost = 25
        self.items_to_luck = [DiamondBoots, DiamondChestplate, DiamondHelmet, Revolver, FireStaff] 
