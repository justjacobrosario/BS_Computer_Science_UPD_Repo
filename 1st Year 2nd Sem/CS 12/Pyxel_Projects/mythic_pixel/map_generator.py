from PIL import Image
from constants import Tile, CELL_PX_SIZE
import importlib
import map_data

def upd_map(map_pic, py_path):
    RGB_TO_TILE = {
        (112, 198, 169):(Tile.GRASS.value), # grass rgb(112, 198, 169)
        (25, 149, 156):(Tile.BUSH.value), # sand rgb(25, 149, 156)
        (163, 163, 163):(Tile.ROCK.value), # snow rgb(163, 163, 163)
        (0, 0, 0):(Tile.NONE.value) # blank rgb(0, 0, 0)
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


    img = Image.open(map_pic).convert("RGB")
    w, h = img.size

    tile_rows = []
    for y in range(h):
        row = []
        for x in range(w):
            rgb = img.getpixel((x, y))
            row.append(nearest_tile(rgb))
        tile_rows.append(row)

    spawn_x, spawn_y, _ = map_pic.split("_")
    cell_px_size = CELL_PX_SIZE
    
    with open(py_path, "w") as f: # to clear it
        pass
    with open(py_path, "w") as f:
        f.write(f"MAP_W = {w}\n")
        f.write(f"MAP_H = {h}\n")
        f.write(f"MAP_DATA = [\n")
        for r in tile_rows:
            f.write(f"    {r},\n")
        f.write("]\n\n")
        f.write(f"PLAYER_PX_SPAWNPOINT = ({int(spawn_x)*cell_px_size}, {int(spawn_y)*cell_px_size})")
    
    importlib.reload(map_data)


if __name__ == "__main__":
    upd_map("15_15_Grasslands.png", "map_data.py")

