import pygame

pygame.init()
pygame.mixer.init()
import config
import random


def play_sound(
    file: str,
    play: bool = True,
    stop_current: bool = True,
    duration: bool = False,
) -> None:
    if stop_current and config.current_sound:
        config.current_sound.stop()
        config.current_sound = False

    if not stop_current:
        my_sound = pygame.mixer.Sound(file)
        my_sound.play() if not duration else my_sound.play(maxtime=duration)
        config.current_sound = my_sound
        return

    if duration:
        my_sound = pygame.mixer.Sound(file)
        my_sound.play(maxtime=duration)
        config.current_sound = False
        return

    if play:
        my_sound = pygame.mixer.Sound(file)
        my_sound.play()
        my_sound.set_volume(config.main_volume / 10)
        config.current_sound = my_sound

def play_sound_fx(
    file: str,
    play: bool = True,
    stop_current: bool = True,
    duration: bool = False,
) -> None:
    if stop_current and config.current_sound:
        config.current_sound_fx.stop()
        config.current_sound_fx = False

    if not stop_current:
        my_sound = pygame.mixer.Sound(file)
        my_sound.play() if not duration else my_sound.play(maxtime=duration)
        config.current_sound_fx = my_sound
        return

    if duration:
        my_sound = pygame.mixer.Sound(file)
        my_sound.play(maxtime=duration)
        config.current_sound_fx = False
        return

    if play:
        my_sound = pygame.mixer.Sound(file)
        my_sound.play()
        my_sound.set_volume(config.main_volume / 10)
        config.current_sound_fx = my_sound


def change_main_vol(new_vol: int) -> None:
    if type(config.current_sound) is bool:
          return
    config.current_sound.set_volume(new_vol / 10)

def change_sound_fx_vol(new_vol: int) -> None:
    if type(config.current_sound_fx) is bool:
          return
    config.current_sound_fx.set_volume(new_vol / 10)


def clicking_sound(stop=False):
    sounds = [config.click_1, config.click_2, config.click_3]
    if stop and config.typing_sound:
        config.typing_sound.stop()
        config.typing_sound = False
        return
    if not stop and config.typing_sound:
        return
    if not config.typing_sound:
        rand = random.randint(0, 2)
        my_sound = pygame.mixer.Sound(sounds[rand])
        my_sound.play()
        config.typing_sound = my_sound
        return


def jeep_sound(stop: bool):
    print(config.jeep_sound)
    if stop:
        config.jeep_sound.stop()
        config.jeep_sound = False
        return
    else:
        my_sound = pygame.mixer.Sound(config.beep_beep)
        my_sound.play()
        my_sound.set_volume(config.sound_fx / 10)
        config.jeep_sound = my_sound
    
def emergency(sound, stop: bool) -> None:
    if stop and type(config.emergency_sound) is not bool:
        config.emergency_sound.stop()
        config.emergency_sound = False
        return
    else:
        my_sound = pygame.mixer.Sound(sound)
        my_sound.play()
        my_sound.set_volume(config.sound_fx / 10)
        config.emergency_sound = my_sound
