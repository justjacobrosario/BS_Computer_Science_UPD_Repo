from constants import Tile

    

class World:
    def __init__(self, screen_width, screen_height, cell_px_size, map_module):

        # MAP PROPERTIES
        self._cell_px_size = cell_px_size
        self.spawn_x, self.spawn_y = (map_module.PLAYER_PX_SPAWNPOINT[0]*cell_px_size, map_module.PLAYER_PX_SPAWNPOINT[1]*cell_px_size)
        self._map_matrix = map_module.MAP_DATA
        self._row_count = len(self._map_matrix)
        self._col_count = len(self._map_matrix[0]) if self._row_count else 0

        # PLAYER PROPERTIES
        self._screen_width = screen_width
        self._screen_height = screen_height
  
    @property
    def col_count(self):
        return self._col_count

    @property
    def row_count(self):
        return self._row_count

    @property
    def map_matrix(self):
        return self._map_matrix
    

    @property
    def screen_width(self):
        return self._screen_width
    
    @property
    def screen_height(self):
        return self._screen_height