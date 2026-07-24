from PIL import Image
from constants import Tile, Cargo
import importlib
import map_data

def upd_map(map_pic, py_path):
    RGB_TO_TILE = {
        (31, 49, 160):(Tile.OCEAN.value), # ocean
        (55, 155, 196):(Tile.SEA.value), # sea
        (58, 141, 9):(Tile.GRASS.value), # grass
        (197, 212, 92):(Tile.SAND.value), # sand
        (255, 255, 255):(Tile.SNOW.value), # snow
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

    with open(py_path, "w") as f:
        f.write(f"MAP_W = {w}\n")
        f.write(f"MAP_H = {h}\n")
        f.write(f"MAP_DATA = [\n")
        for r in tile_rows:
            f.write(f"    {r},\n")
        f.write("]\n\n")
        f.write(f"PLAYER_PX_SPAWNPOINT = ({spawn_x}, {spawn_y})")
    
    importlib.reload(map_data)


if __name__ == "__main__":
    upd_map("720_180_SoutheastMap.png", "map_data.py")

