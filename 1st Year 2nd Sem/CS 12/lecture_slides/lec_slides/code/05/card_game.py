from dataclasses import dataclass
from enum import Enum, auto
 
 
class Suit(Enum):
    HEART = auto()
    SPADE = auto()
    DIAMOND = auto()
    CLUB = auto()
 
 
class Rank(Enum):
    TWO = auto()
    THREE = auto()
    ...
    KING = auto()
 
 
@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank
 
 
class Deck:
    def __init__(self):
        self._cards = [Card(suit, rank) for suit in Suit for rank in Rank]
 
 
class BlackJackGame:
    def __init__(self):
        self._deck = Deck()
