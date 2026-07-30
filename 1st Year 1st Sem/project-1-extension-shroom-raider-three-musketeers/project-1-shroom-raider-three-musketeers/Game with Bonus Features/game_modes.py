import animations
import random
import game
import winner
import lose
import config
import time
import data


def speedrun_mode() -> None:
    stages = [
        config.stage_1,
        config.stage_2,
        config.stage_3,
        config.stage_4,
        config.stage_5,
        config.stage_6,
        config.stage_7,
        config.stage_8,
        config.stage_9,
        config.stage_10,
        config.stage_12,
        config.stage_13,
        config.stage_14,
        config.stage_15,
        config.stage_16,
        config.stage_17,
        config.stage_18,
        config.stage_19,
        config.stage_20,
    ]

    speedrun_maps = []
    start = time.time()

    for _ in range(10):
        random_map = random.randint(0, len(stages) - 1)
        print(random_map)
        speedrun_maps.append(stages[random_map])
        stages.pop(random_map)

    for m in speedrun_maps:
        if game.new_game(stage=m):
            continue
        else:
            return lose.lose()
    
    if config.current_user != 'GUEST':
        data.modify_db(int(time.time() - start), 'database.db', config.current_user)
    winner.winner()

def story_mode() -> None:
    stages = [
        config.stage_1,
        config.stage_2,
        config.stage_3,
        config.stage_4,
        config.stage_5,
        config.stage_6,
        config.stage_7,
        config.stage_8,
        config.stage_9,
        config.stage_10,
        config.stage_12,
        config.stage_13,
        config.stage_14,
        config.stage_15,
        config.stage_16,
        config.stage_17,
        config.stage_18,
        config.stage_19,
        config.stage_20,
    ]


    animations.intro_cutscene()
    animations.aech_intro()
    if not game.new_game(stage=stages[0]):
        return
    animations.aech_end()
    animations.eee_intro()
    if not game.new_game(stage=stages[1]):
        return
    animations.msi_intro()
    if not game.new_game(stage=stages[2]):
        return
    animations.palma_intro()
    if not game.new_game(stage=stages[3]):
        return
    animations.dorms_intro()
    if not game.new_game(stage=stages[4]):
        return
    animations.upis_intro()
    if not game.new_game(stage=stages[5]):
        return
    animations.sunken_intro()
    if not game.new_game(stage=stages[6]):
        return
    animations.econ_intro()
    if not game.new_game(stage=stages[7]):
        return
    animations.econ_end()
    animations.iirh_intro()
    if not game.new_game(stage=stages[8]):
        return
    animations.uhs_intro()
    if not game.new_game(stage=stages[9]):
        return
    animations.acacia_intro()
    if not game.new_game(stage=stages[10]):
        return
    animations.a2_intro()
    if not game.new_game(stage=stages[11]):
        return
    animations.melchor_intro()
    if not game.new_game(stage=stages[12]):
        return
    animations.melchor_end()
    animations.alumni_intro()
    if not game.new_game(stage=stages[13]):
        return
    animations.chk_intro()
    if not game.new_game(stage=stages[14]):
        return
    animations.solair_intro()
    if not game.new_game(stage=stages[15]):
        return
    animations.oblation_intro()
    if not game.new_game(stage=stages[16]):
        return
    animations.gyudfood_intro()
    if not game.new_game(stage=stages[17]):
        return
    animations.hda_intro()
    if not game.new_game(stage=stages[18]):
        return
    animations.knl_intro()
    if not game.new_game(stage=stages[19]):
        return
    animations.end_cutscene()

