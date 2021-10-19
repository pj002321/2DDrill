from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100,700)
        self.y = 90
        self.frame = random.randint(0,7)
        self.imageball21x21 = load_image('ball21X21.png')
        self.imageball41x41 = load_image('ball41X41.png')
        self.b1_x = random.randint(10,700)
        self.b1_y = 599
        self.b1_frame = random.randint(0, 8)
        self.b2_x = random.randint(10,700)
        self.b2_y = 599
        self.b2_frame = random.randint(0, 8)

    def update(self):

        self.x += 3
        self.frame = (self.frame + 1)%8
        if self.b1_y <=80 and self.b1_y>=70:
            self.b1_y =70
        else:
            self.b1_y -= random.randint(1, 6)
        if self.b2_y <= 75 and self.b2_y >= 60:
            self.b2_y = 60
        else:
            self.b2_y -= random.randint(1, 6)


    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

        self.imageball41x41.draw(self.b1_x,self.b1_y)
        self.imageball21x21.draw(self.b2_x, self.b2_y)







def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code 초기화 객체생성
open_canvas()
grass = Grass()
team=[Boy() for i in range(10)]


running = True
# game main loop code
while running:
    handle_events()
    #Game Logic : 상호작용
    for boy in team:
        boy.update()

    #Game Drawing : 그리기
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    delay(0.05)
# finalization code

close_canvas()