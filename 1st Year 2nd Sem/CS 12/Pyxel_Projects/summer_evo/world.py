import pyxel
from enum import Enum, auto
from player import Player, Animal, Key_Input
from random import choice
from abc import ABC
from plants import Plant_Type, Plant

class Tile_type(Enum):
    WATER = "🟦"
    GRASS = "🟩"
    SAND = "🟨"
    MUD = "🟫"

class Biome(Enum):
    OCEAN = "water_coords"
    GRASSY = "grass_coords"
    DESERT = "sand_coords"
    MUDDY = "mud_coords"
    




class PlantsGenerator():
    def __init__(self, width, height, row_count, col_count, map_coords_dict):
        self._width = width
        self._height = height
        self._row_count = row_count
        self._col_count = col_count
        self._map_coords_dict = map_coords_dict

        self._plants_coords_dict = {
        "grass_plants" : [],
        "sand_plants" : [],
        "water_plants" : [],
        "mud_plants" : []
        }

        self._plants_list = []


    @property
    def plants_coords_dict(self):
        return self._plants_coords_dict

    @property
    def plants_list(self):
        return self._plants_list


    def spawn_biome_plants(self, count, biome):
        biome_coords_list = self._map_coords_dict[biome.value]

        free_space = []

        biome_plant_mapping = {Biome.GRASSY : "grass_plants", Biome.OCEAN : "water_plants", Biome.DESERT : "sand_plants", Biome.MUDDY : "mud_plants"}
        selected_biome_section = biome_plant_mapping[biome]

        for r, c in biome_coords_list:
            if (r, c) not in self._plants_coords_dict[selected_biome_section]:
                free_space.append((r,c))

        biome_plants_options = {
            "grass_plants" : [Plant_Type.OAK_TREE, Plant_Type.BERRY_BUSH, Plant_Type.FLOWER_MARIGOLD, Plant_Type.FLOWER_SUNFLOWER, Plant_Type.JUST_BUSH],
            "water_plants" : [Plant_Type.CORAL_RED, Plant_Type.CORAL_VIOLET, Plant_Type.CORAL_YELLOW, Plant_Type.SEAWEED],
            "sand_plants" : [Plant_Type.CACTUS, Plant_Type.JOSHUA_TREE],
            "mud_plants" : [Plant_Type.CATTAIL, Plant_Type.SEDGES_WEED, Plant_Type.ELEPHANTS_EAR]
            }

        chosen_coords = []
        for _ in range(count):
            if free_space:
                coord = choice(free_space)
                plant_r, plant_c = coord
                free_space.remove(coord)
                self._plants_coords_dict[selected_biome_section].append(coord)

                p_type = choice(biome_plants_options[selected_biome_section])

                plant_info = p_type.value

                exp = plant_info["exp"]
                who_can_eat = plant_info["who_can_eat"]
                base_hp = plant_info["base_hp"]
                maturity_age = plant_info["maturity_age"]
                lifespan = plant_info["lifespan"]

                new_plant = Plant(p_type, exp, who_can_eat, base_hp, maturity_age, lifespan, plant_r, plant_c)
                self._plants_list.append(new_plant)

    



class World:
    def __init__(self, width, height, map_path):


        self._width = width
        self._height = height

        def parse_map(filename): # returns (l_col, l_row, map_coords_dict)
            with open(filename, "r", encoding = "utf-8") as f:
                lines = f.read().splitlines()[1:]

            # coord is in (row, col)
            water_coords, grass_coords, mud_coords, sand_coords = ([], [], [], [])

            l_col = len(lines[0])
            for r, row in enumerate(lines):
                for c, col in enumerate(row):
                    if lines[r][c] == Tile_type.WATER.value:
                        water_coords.append((r, c))
                    elif lines[r][c] == Tile_type.GRASS.value:
                        grass_coords.append((r, c))
                    elif lines[r][c] == Tile_type.SAND.value:
                        sand_coords.append((r, c))
                    elif lines[r][c] == Tile_type.MUD.value:
                        mud_coords.append((r, c))


            return (l_col, len(lines), {"water_coords" : water_coords, "grass_coords" : grass_coords, "mud_coords" : mud_coords, "sand_coords" : sand_coords})

        self._col_count, self._row_count, self._map_coords_dict = parse_map(map_path)
        self._player = Player(self._width // 2, self._height // 2)


        self._plants_generator = PlantsGenerator(self._width, self._height, self._row_count, self._col_count, self._map_coords_dict)

        plant_vol = 0.10
        for biome, count in zip([Biome.GRASSY, Biome.OCEAN, Biome.DESERT, Biome.MUDDY], [len(self._map_coords_dict["grass_coords"]) * plant_vol, len(self._map_coords_dict["water_coords"]) * plant_vol, len(self._map_coords_dict["sand_coords"]) * plant_vol, len(self._map_coords_dict["mud_coords"]) * plant_vol]):
            self._plants_generator.spawn_biome_plants(int(count//1), biome)


    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def map_coords_dict(self):
        return self._map_coords_dict

    @property
    def col_count(self):
        return self._col_count

    @property
    def row_count(self):
        return self._row_count

    @property
    def player(self):
        return self._player

    @property
    def plants_generator(self):
        return self._plants_generator
    
    

                



        
        
        
        



