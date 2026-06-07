Position = 'a1' | 'a2' | ... | 'h7' | 'h8'
 


class Chessboard:
    def get_position(self, position: Position):
        ...


class Player:
    def get_next_action(self, chessboard: Chessboard):
        ...


class BoardToChessboardAdapter(Chessboard):
    def __init__(self, board: Board):
        self._board = board
 
    def get_position(self, position: Position):
        x, y = self._position_to_cell(position)
        return self._board.get_cell(x, y)
 
    # ...
 

class Board:
    def get_cell(self, x: int, y: int):
        ...
