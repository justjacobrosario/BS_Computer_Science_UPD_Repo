# ===== [ CURRENT LANGUAGE ] ===== #

chosen_lang = "english"


def translate(eng_trans, jap_trans, fil_trans, chosen_lang):
    if chosen_lang == "english":
        return eng_trans
    elif chosen_lang == "japanese":
        return jap_trans
    elif chosen_lang == "filipino":
        return fil_trans


# ===== [ GLOBAL CONSTANTS ] ===== #

TREE = "T"
PLAYER = "L"
ROCK = "R"
WATER = "~"
MUSHROOM = "+"
PAVED = "-"
AXE = "A"
FLAMETHROWER = "F"
HAMMER = "H"
player_charac = "🧑"


BRICK = "B"
ROOF = "Y"
CONCRETE = "C"
STREET = "S"


# ===== [ GLOBAL VARIABLES ] ===== #

total_mush = 0
mush_count = 0
paved_tiles = {}
standing_on_item = "."
item_on_ground_prompt = " "
held_item = " "
current_user = "GUEST"
current_sound = False
current_sound_fx = False
typing_sound = False
jeep_sound = False
emergency_sound = False
main_volume = 5
sound_fx = 5

# ===== [ UI COLORS ] ===== #

map_line_color = 0
map_bg_color = 2
line_color = 0
bg_color = 7


# ===== [ SOUNDTRACKS ] ===== #

menu_sound = "andromeda-space-adventure-403080.mp3"
lose_sound = "gta-v-wasted-death-sound.mp3"
win_sound = "victory-chime-366449.mp3"
click_sound = "shine-1-268902.mp3"
space_sound = "ambience-brisk-walking-on-dry-grass-with-late-night-soundscape-7948.mp3"
rock_push_sound = "dropping-rocks-5996.mp3"
rock_push_water_sound = "water-splash-46402.mp3"
burning_sound = "designed-fire-winds-swoosh-04-116788.mp3"
chop_sound = "hand-saw-cutting-tree-2-230185.mp3"
mushroom_collect_sound = "sound-effect-twinklesparkle-115095.mp3"
click_1 = "keyboard-typing-fast-371229.mp3"
click_2 = "keyboard-typing-5997.mp3"
click_3 = "typing-6458.mp3"
beep_beep = "JEEP HORN SOUND.mp3"
wee_woo = "security-alarm-63578.mp3"
take_off = "rocket-launch-sfx-253937.mp3"

# ==== [ MAPS ] ====


stage_1 = '30 70 1.txt'
stage_2 = '30 70 2.txt'
stage_3 = '30 70 3.txt'
stage_4 = '30 70 4.txt'
stage_5 = '30 70 5.txt'
stage_6 = '30 70 6.txt'
stage_7 = '30 70 7.txt'
stage_8 = '30 70 8.txt'
stage_9 = '30 70 9.txt'
stage_10 = '30 70 10.txt'
stage_11 = '30 70 11.txt'
stage_12 = '30 70 12.txt'
stage_13 = '30 70 13.txt'
stage_14 = '30 70 14.txt'
stage_15 = '30 70 15.txt'
stage_16 = '30 70 16.txt'
stage_17 = '30 70 17.txt'
stage_18 = '30 70 18.txt'
stage_19 = '30 70 19.txt'
stage_20 = '30 70 19.txt'


