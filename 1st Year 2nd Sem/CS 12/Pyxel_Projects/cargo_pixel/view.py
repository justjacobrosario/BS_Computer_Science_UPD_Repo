from map_data import MAP_DATA, MAP_W, MAP_H
from collections import Counter

flat = [tile for row in MAP_DATA for tile in row]
print(Counter(flat))