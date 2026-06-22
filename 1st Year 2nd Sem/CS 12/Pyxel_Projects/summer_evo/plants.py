from enum import Enum, auto
from constants import Animal



class Plant_Type(Enum): # make another intenum with u,v sprite coords in view
    OAK_TREE = {
        "name" : "OAK_TREE",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    BERRY_BUSH = {
        "name" : "BERRY_BUSH",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    FLOWER_MARIGOLD = {
        "name" : "FLOWER_MARIGOLD",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    FLOWER_SUNFLOWER = {
        "name" : "FLOWER_SUNFLOWER",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    JUST_BUSH = {
        "name" : "JUST_BUSH",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }

    CATTAIL = {
        "name" : "CATTAIL",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    SEDGES_WEED = {
        "name" : "SEDGES_WEED",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    ELEPHANTS_EAR = {
        "name" : "ELEPHANTS_EAR",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }

    CACTUS = {
        "name" : "CACTUS",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    JOSHUA_TREE = {
        "name" : "JOSHUA_TREE",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }

    CORAL_RED = {
        "name" : "CORAL_RED",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    CORAL_VIOLET = {
        "name" : "CORAL_VIOLET",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    CORAL_YELLOW = {
        "name" : "CORAL_YELLOW",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }
    SEAWEED = {
        "name" : "SEAWEED",
        "exp" : 10,
        "who_can_eat" : [Animal.ALL],
        "base_hp" : 50,
        "maturity_age" : 36,
        "lifespan" : 60
        }


class Plant_Age_Phase(Enum):
    YOUNG = auto()
    MATURED = auto()
    OLD = auto()


class Plant():
    def __init__(self, plant_type, exp, who_can_eat, base_hp, maturity_age, lifespan, r, c):
        self._plant_type = plant_type
        self._r = r
        self._c = c

        self._exp = exp
        self._who_can_eat = who_can_eat
        self._base_hp = base_hp
        self._maturity_age = maturity_age # when sapling becomes mature
        self._lifespan = lifespan

        self._curr_hp = base_hp
        self._curr_age = 0

        self._age_phase = Plant_Age_Phase.YOUNG


    @property
    def plant_type(self):
        return self._plant_type

    @property
    def r(self):
        return self._r
    
    @property
    def c(self):
        return self._c
    

    @property
    def exp(self):
        return self._exp
    
    @property
    def who_can_eat(self):
        return self._who_can_eat
    
    @property
    def base_hp(self):
        return self._base_hp
    
    @property
    def maturity_age(self):
        return self._maturity_age
    
    @property
    def lifespan(self):
        return self._lifespan
    
    @property
    def curr_hp(self):
        return self._curr_hp

    @property
    def curr_age(self):
        return self._curr_age

    @property
    def age_phase(self):
        return self._age_phase
    
    def dec_hp(self, val):
        self._curr_hp -= val

    def upd_age(self, val):
        self._curr_age += val

        if self._curr_age < self._maturity_age:
            self._age_phase = Plant_Age_Phase.YOUNG
        elif self._curr_age > (self._lifespan * 0.9): # if 90%+ old in its lifespan
            self._age_phase = Plant_Age_Phase.OLD
        else:
            self._age_phase = Plant_Age_Phase.MATURED


    def receive_exp(self):
        multiplier = { 
            Plant_Age_Phase.YOUNG : 0.1, 
            Plant_Age_Phase.MATURED : 1,
            Plant_Age_Phase.OLD : 0.5
        }

        return self._exp * multiplier[self._age_phase]


    