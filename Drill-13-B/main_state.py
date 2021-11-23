import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from brick import Brick
from ball import Ball
name = "MainState"

boy = None
grass = None
balls = []
bricks = []

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def collideball(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    if bottom_a > top_b: return False
    if top_a < bottom_b: return False
    return True



def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global bricks
    bricks = [Brick(300+300*i, 100+50*i) for i in range(5)]
    game_world.add_objects(bricks, 1)



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
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for brick in bricks:
        for ball in balls:
            if collide(ball, brick):
                ball.stop()
                ball.x=clamp(brick.x-60,ball.x,brick.x+60)
                ball.y = clamp(brick.y+30, ball.y, ball.y+30)
                if collide(ball, ball):
                    ball.stop()


    for brick in bricks:
        if collide(boy,brick):
            boy.stop()
            boy.y = clamp(brick.y + 50, boy.y, brick.y + 50)
            boy.x = clamp(brick.x - 60, boy.x, brick.x + 60)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






