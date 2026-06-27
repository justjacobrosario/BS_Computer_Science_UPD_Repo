from PIL import Image



class world:
    def __init__(self, screen_width, screen_height, map_path):

        # MAP PROPERTIES
        self._map_path = map_path

        def upd_map():
            RGB_TO_TILE = {
                (31, 49, 160):0, # ocean
                (55, 155, 196):1, # sea
                (58, 141, 9):2, # grass
                (197, 212, 92):3, # sand
                (255, 255, 255):4 # snow
            }
            def nearest_tile(curr_rgb):
                '''
                in a pixel's rgb, get the nearest tile from the RGB_TO_TILE dict
                '''
                closest_tile, best_dist = 0, float("inf")
                for reference, tile in RGB_TO_TILE.items():
                    dist = sum((curr-ref)**2 for curr, ref in zip(curr_rgb, reference) )

                    if dist < best_dist:
                        closest_tile, best_dist = tile, dist
                return closest_tile


            img = Image.open(self._map_path).convert("RGB")
            w, h = img.size

            map_data = []
            for y in range(h):
                row = []
                for x in range(w):
                    rgb = img.getpixel((x, y))
                    row.append(nearest_tile(rgb))
                map_data.append(row)

            with open("map_data.py", "w") as f:
                f.write(f"MAP_W = {w}\n")
                f.write(f"MAP_H = {w}\n")
                f.write(f"MAP_DATA = [\n")
                for r in map_data:
                    f.write(f"    {r},\n")
                f.write("]\n")

        upd_map()
        self.upd_map = upd_map

        def get_col_row_count():
            with open("map_data.py", "r") as f:
                _, _, w = f.readline() # reads 1st line
                _, _, h = f.readline() # 2nd line

            return (int(w), int(h))
        self._col, self._row = get_col_row_count()


        # PLAYER PROPERTIES
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._player = Player(self._screen_width//2, self._screen_height//2, 0)

    @property
    def map_path(self):
        return self._map_path

    @property
    def col(self):
        return self._col

    @property
    def row(self):
        return self._row

    @property
    def screen_width(self):
        return self._screen_width
    
    @property
    def screen_height(self):
        return self._screen_height
    
    
    
        