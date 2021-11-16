
from pico2d import *

import BirdFly
import game_framework
import game_world

from Bird import Bird
from grass import Grass


name = "MainState"

bird = None
grass = None
balls = []
big_balls = []


def collide(a, b):
    # fill here
    return True




def enter():
    global bird
    bird = Bird()

    game_world.add_object(bird, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls





def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()



def update():
    for game_object in game_world.all_objects():
        BirdFly.birds.update()
        game_object.update()
    delay(0.05)
    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






