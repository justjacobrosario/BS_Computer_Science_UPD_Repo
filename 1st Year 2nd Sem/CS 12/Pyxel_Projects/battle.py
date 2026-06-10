from abc import ABC, abstractmethod
from random import shuffle
from dataclasses import dataclass

@dataclass
class Berry:
    name: str
    hp_delta: int

type BerryBag = list[Berry]

####
class Pokemon:
    def __init__(self, name : str, hp : int, berry_bag : Berry | None)  -> None:
        self.name = name
        self.hp = hp
        self.__berry_bag = berry_bag
    
    @property
    def get_berry_bag(self) -> BerryBag | None:
        return self.__berry_bag

    def gain_hp(self, delta : int) -> None:
        self.hp += delta
    
    def throw(self, target : Pokemon) -> None:
        if self.__berry_bag:
            berry : Berry = self.__berry_bag.pop()
            target.gain_hp(berry.hp_delta)
    
    def jumble(self) -> None:
        if self.__berry_bag:
            shuffle(self.__berry_bag)

    def is_alive(self) -> None:
        return self.hp > 0

class MainPokemon(Pokemon):
    def __init__(self, name : str, hp : int, berry_bag : Berry)  -> None:
        super().__init__(name, hp, berry_bag)

class GreedyPokemon(MainPokemon):
    def throw(self, target : Pokemon) -> None:
        pass
    
    def jumble(self) -> None:
        pass

    @property
    def get_berry_bag(self) -> BerryBag | None:
        pass
####



####
class SupportPokemon(Pokemon):
    def eat_from_berry_bag_of(self, target : MainPokemon):
        targets_bag : BerryBag | None  = target.get_berry_bag
        if len(targets_bag) > 0:
            stolen_berry : Berry = targets_bag.pop()
            self.gain_hp(stolen_berry.hp_delta)

class SuperSupportPokemon(SupportPokemon):
    def eat_from_berry_bag_of(self, target : MainPokemon):
        targets_bag : BerryBag | None  = target.get_berry_bag
        if len(targets_bag) > 0:
            for _ in range(min(2, len(targets_bag))):
                stolen_berry : Berry = targets_bag.pop()
                self.gain_hp(stolen_berry.hp_delta)
####



class PokemonTeam(ABC):
    def __init__(self, m : MainPokemon, s : SupportPokemon) -> None:
        self.m = m
        self.s = s

    @abstractmethod
    def get_main(self) -> MainPokemon:
        pass

    @abstractmethod
    def get_support(self) -> SupportPokemon:
        pass

    
class ChallengerTeam(PokemonTeam):
    def get_main(self) -> MainPokemon:
        return self.m
    def get_support(self) -> SupportPokemon:
        return self.s

class LeaderTeam(PokemonTeam):
    def __init__(self, m : MainPokemon, s : SuperSupportPokemon) -> None:
        super().__init__(m, s)

    def get_main(self) -> MainPokemon:
        return self.m
    def get_support(self) -> SuperSupportPokemon:
        return self.s