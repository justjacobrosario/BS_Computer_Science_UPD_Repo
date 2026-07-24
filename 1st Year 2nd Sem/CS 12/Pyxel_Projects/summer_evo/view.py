import pyxel
from enum import IntEnum, Enum, auto
from plants import Plant_Type, Plant
from constants import Key_Input, Color




class View:
    def start(self, screen_width, screen_height):
        pyxel.init(screen_width, screen_height, title="Summer Evolution")
        pyxel.load("audio_visuals.pyxres")

    def get_key_input(self):
        if pyxel.btn(pyxel.KEY_Q):
            return Key_Input.QUIT
        elif pyxel.btn(pyxel.KEY_W):
            return Key_Input.GO_UP
        elif pyxel.btn(pyxel.KEY_S):
            return Key_Input.GO_DOWN
        elif pyxel.btn(pyxel.KEY_A):
            return Key_Input.GO_LEFT
        elif pyxel.btn(pyxel.KEY_D):
            return Key_Input.GO_RIGHT
        elif pyxel.btn(pyxel.KEY_UP):
            return Key_Input.GO_UP_2
        elif pyxel.btn(pyxel.KEY_DOWN):
            return Key_Input.GO_DOWN_2
        elif pyxel.btn(pyxel.KEY_LEFT):
            return Key_Input.GO_LEFT_2
        elif pyxel.btn(pyxel.KEY_RIGHT):
            return Key_Input.GO_RIGHT_2
        else:
            return Key_Input.NONE





    def draw_grid(self, screen_width, screen_height, row_count, col_count, cell_px_size):
        vertical_offset = (screen_height - (row_count * cell_px_size)) // 2
        horizontal_offset = (screen_width - (col_count * cell_px_size)) // 2

        for row in range(row_count):
            for col in range(col_count):
                x = horizontal_offset + col * cell_px_size
                y = vertical_offset + row * cell_px_size

                if (row + col) % 2 == 0:
                    pyxel.rect(x, y, cell_px_size, cell_px_size, 7)  # Draw a white rectangle for each grid cell
                else:
                    pyxel.rect(x, y, cell_px_size, cell_px_size, 8)  # Draw a yellow rectangle for each grid cell


    '''def draw_grid_map(self, screen_width, screen_height, row_count, col_count, cell_px_size, map_coords_dict):
                    vertical_offset = (screen_height - (row_count * cell_px_size)) // 2
                    horizontal_offset = (screen_width - (col_count * cell_px_size)) // 2
            
                    for row in range(row_count):
                        for col in range(col_count):
                            x = horizontal_offset + col * cell_px_size
                            y = vertical_offset + row * cell_px_size
            
                            if (row, col) in map_coords_dict["water_coords"]:
                                pyxel.rect(x, y, cell_px_size, cell_px_size, Color.BLUE)
                            elif (row, col) in map_coords_dict["grass_coords"]:
                                pyxel.rect(x, y, cell_px_size, cell_px_size, Color.GREEN)
                            elif (row, col) in map_coords_dict["sand_coords"]:
                                pyxel.rect(x, y, cell_px_size, cell_px_size, Color.YELLOW)
                            elif (row, col) in map_coords_dict["mud_coords"]:
                                pyxel.rect(x, y, cell_px_size, cell_px_size, Color.BROWN)
                            else:
                                pyxel.rect(x, y, cell_px_size, cell_px_size, Color.BLACK)'''

    def draw_grid_map(self, screen_width, screen_height, row_count, col_count, cell_px_size, map_coords_dict, player_x, player_y):
        center_x = screen_width // 2
        center_y = screen_height // 2

        cam_offset_x = (center_x - player_x)
        cam_offset_y = (center_y - player_y)

        pyxel.cls(0)

        tile_sprites = {
        "blank" : (0, 0),
        "grass" : (16, 0),
        "water" : (32, 0),
        "sand" : (48, 0),
        "mud" : (0, 16)
        }


        for row in range(row_count):
            for col in range(col_count):

                x = (col * cell_px_size) + cam_offset_x
                y = (row * cell_px_size) + cam_offset_y

                #if the tile is fully off-screen, skip drawing it
                if x < -cell_px_size or x > screen_width or y < -cell_px_size or y > screen_height:
                    continue

                if (row, col) in map_coords_dict["water_coords"]:
                    u, v = tile_sprites["water"]
                elif (row, col) in map_coords_dict["grass_coords"]:
                    u, v = tile_sprites["grass"]
                elif (row, col) in map_coords_dict["sand_coords"]:
                    u, v = tile_sprites["sand"]
                elif (row, col) in map_coords_dict["mud_coords"]:
                    u, v = tile_sprites["mud"]
                else:
                    u, v = tile_sprites["blank"]

                pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size)



    def draw_plants(self, screen_width, screen_height, row_count, col_count, cell_px_size, plants_list, player_x, player_y):
        center_x = screen_width // 2
        center_y = screen_height // 2

        cam_offset_x = (center_x - player_x)
        cam_offset_y = (center_y - player_y)

        #pyxel.cls(0)
        
        tile_map_coord_dict = {
            Plant_Type.OAK_TREE : (0,0),
            Plant_Type.BERRY_BUSH : (0,16),
            Plant_Type.FLOWER_MARIGOLD : (0,32),
            Plant_Type.FLOWER_SUNFLOWER : (0,48),
            Plant_Type.JUST_BUSH : (0,64),

            Plant_Type.CATTAIL : (0,80),
            Plant_Type.SEDGES_WEED : (0,96),
            Plant_Type.ELEPHANTS_EAR : (0,112),

            Plant_Type.CACTUS : (0,128),
            Plant_Type.JOSHUA_TREE : (0,144),

            Plant_Type.CORAL_RED : (0,160),
            Plant_Type.CORAL_VIOLET : (0,176),
            Plant_Type.CORAL_YELLOW : (0,192),
            Plant_Type.SEAWEED : (0,208)
        }

        for plant in plants_list:
            row, col = (plant.r, plant.c)

            x = (col * cell_px_size) + cam_offset_x
            y = (row * cell_px_size) + cam_offset_y

            #if the tile is fully off-screen, skip drawing it
            if x < -cell_px_size or x > screen_width or y < -cell_px_size or y > screen_height:
                continue

            u, v = tile_map_coord_dict[plant.plant_type]

            pyxel.blt(x, y, 1, u, v, cell_px_size, cell_px_size, Color.DARK_BLUE)
            #pyxel.rect(x, y, cell_px_size, cell_px_size, Color.RED)





    def draw_player(self, screen_width, screen_height, cell_px_size):
        tl_x = screen_width//2 - (cell_px_size // 2)
        tl_y = screen_height//2 - (cell_px_size // 2)
        pyxel.blt(tl_x, tl_y, 0, 32, 16, cell_px_size, cell_px_size, Color.DARK_BLUE)

    def clear(self):
        pyxel.cls(0)
