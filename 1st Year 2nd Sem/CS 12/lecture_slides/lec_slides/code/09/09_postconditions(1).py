class DeckManagerV1:
    def random(self, seed: int) -> Deck:
        """Return a randomized nonempty `Deck`."""
        ...

class DeckManagerV2A(DeckManagerV1):
    def random(self, seed: int) -> Deck:
        """Return a randomized nonempty `Deck`
        containing only face cards."""
        ...

class DeckManagerV2B(DeckManagerV1):
    def random(self, seed: int) -> Deck:
        """Return a randomized `Deck`."""
        ...

# DeckManagerV2A <: DeckManagerV1
# DeckManagerV2B <: DeckManagerV1
 
def client(manager: DeckManagerV1):
    deck = manager.random()
    x = deck.draw()
    ...
 
v1 = DeckManagerV1()
v2a = DeckManagerV2A()
v2b = DeckManagerV2B()
 
client(v1)
client(v2a)
client(v2b)