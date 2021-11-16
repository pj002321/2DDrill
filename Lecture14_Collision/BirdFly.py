import random
from pico2d import *

# 새의 크기는 100X100 pixcel이며 픽셀당 0.04mX0.04 입니다.
# 새의 속도는 시간당 60km 속도로 구현을 하였습니다.
import game_framework

PIXEL_PER_METER = (10.0 / 0.4)  # 10 pixel 40 cm
FLY_SPEED_KMPH = 60.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 14
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)


class Bird:

    def __init__(self):
        self.i=0
        self.x = [random.randint(100,700) for self.i in range(6)]

        self.y = random.randint(300, 550)
        self.frame = 0
        self.image = load_image('bird100X100X14.png')
        self.dir=random.randint(1,2)
    def update(self):

        self.frame = (self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%14
        if self.dir==1:
            self.x[self.i] += FLY_SPEED_PPS

            if self.x[self.i]>=750:
                self.x[self.i] -= FLY_SPEED_PPS
                self.dir=2

        if self.dir==2:

            self.x[self.i] -= FLY_SPEED_PPS

            if self.x[self.i]<=50:
                self.x[self.i] += FLY_SPEED_PPS
                self.dir=1

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x[self.i], self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

birds = [Bird() for i in range(5)]


grass = Grass()

running = True;
while running:
    handle_events()
    for bird in birds:
        bird.update()

    clear_canvas()
    grass.draw()
    for bird in birds:
        bird.draw()
    delay(0.05)
    update_canvas()
close_canvas()
