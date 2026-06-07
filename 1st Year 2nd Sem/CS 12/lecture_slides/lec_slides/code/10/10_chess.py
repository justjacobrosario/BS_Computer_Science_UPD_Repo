Position = 'a1' | 'a2' | ... | 'h7' | 'h8'
 

class Chessboard:
    def get_position(self, position: Position):
        ...


class Player:
    def get_next_action(self, chessboard: Chessboard):
        ...


class Board:
    def get_cell(self, x: int, y: int):
        ...
