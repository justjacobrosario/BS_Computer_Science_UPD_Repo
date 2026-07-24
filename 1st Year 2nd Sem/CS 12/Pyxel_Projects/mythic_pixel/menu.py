from enum import IntEnum
from stages import Difficulty, Stage, Grasslands, Drylands, Winterlands
from random import randint
from items import Item, Helmet, Chestplate, Boots, Weapon

class DifficultyOrder(IntEnum):
    Normal = 1
    Hard = 1
    Nightmare = 3

STAGE_ORDER = {
    Grasslands: 1,
    Drylands: 2,
    Winterlands:3
}


class Account:
    def __init__(self, username:str):

        self.x, self.y = (0,0)
        self.username : str = username

        # recorded properties
        self.latest_stage : tuple[type[Stage], DifficultyOrder] = (Grasslands, DifficultyOrder.Normal)
        self.keys : int = 0
        self.exp : int = 0
        self.lvl : int = 0
        self.inventory : set[Item] = set()

        # ingame properties
        self.speed : int = 1

        # equipped things
        self.equipped_helmet : Helmet | None = None
        self.equipped_chestplate : Chestplate | None = None
        self.equipped_boots : Boots | None = None
        self.equipped_weapons : list[Weapon | None] = [None]


class Menu:
    def __init__(self):

        self.chosen_stage : None | Stage = None
        self.chosen_difficulty : DifficultyOrder | None = None
        self.online_accounts : set[Account] = set()


    def is_stage_unlocked(self, account: Account, target_stage : type[Stage], target_diff: DifficultyOrder) -> bool:
        latest_stage_cls, latest_diff = account.latest_stage

        target_stage_rank = STAGE_ORDER[target_stage]
        latest_stage_rank = STAGE_ORDER[latest_stage_cls]

        if target_stage_rank < latest_stage_rank:
            return True

        elif target_stage_rank == latest_stage_rank:
            return (target_diff <= latest_diff)

        else:
            return False


    def change_stage(self, account: Account, target_stage: type[Stage], target_diff: DifficultyOrder) -> bool:
        if self.is_stage_unlocked(account, target_stage, target_diff):
            self.chosen_stage = target_stage()
            self.chosen_difficulty = target_diff
            return True # successful change stage
        else:
            return False
        
