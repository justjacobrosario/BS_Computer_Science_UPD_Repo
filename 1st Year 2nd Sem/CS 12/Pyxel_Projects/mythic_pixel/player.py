from enum import Enum

class Player:
    def __init__(self, x, y, lvl):
        self.x = x
        self.y = y

        
        self._speed = 10
        self._hp = 100
        self._exp = 0
        self._is_dead = False
    

    @property
    def hp(self):
        return self._hp

    @property
    def speed(self):
        return self._speed

    @property
    def exp(self):
        return self._exp


    @exp.setter
    def exp(self, val):
        self._exp = val


    
    
    
    
    
    

