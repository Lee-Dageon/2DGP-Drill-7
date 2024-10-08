from pico2d import *
from pygame.display import update
import random

class Grass:
    #생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self): #아주 기본적인 객체 self
        # 모양 없는 납작한 붕어빵의 초기 모습 결정
        self.image = load_image('grass.png')

    def update(self): #Shift + Enter
        pass

    def draw(self):
        self.image.draw(400,30)

    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,700),90
        self.frame=0
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8  # 일정한 속도로 프레임 증가
        self.x += 5  # 캐릭터의 x 좌표를 일정하게 증가시켜 이동

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


# Game object class here
class Bigball:
    #생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self): #아주 기본적인 객체 self
        # 모양 없는 납작한 붕어빵의 초기 모습 결정
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 800), 599

    def update(self): #Shift + Enter
        if self.y > 60:
            self.y-=random.randint(1,20)

    def draw(self):
        self.image.draw(self.x, self.y)

    pass

class Smallball:
    def __init__(self):
        self.x, self.y = random.randint(0,800),599
        self.frame=0
        self.image=load_image('ball21x21.png')

    def update(self):
        if self.y > 60:
            self.y-=random.randint(1,20)

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global boy
    global smallball
    global bigball
    global team_small
    global team_big
    global world

    world = []
    grass = Grass()  # 잔디를 찍어낸다. 생성한다.
    world.append(grass)
    team = [Boy() for i in range(10)]
    world += team

    running = True

    smallball = Smallball() #잔디를 찍어낸다. 생성한다.
    bigball = Bigball()
    world.append(smallball)
    world.append(bigball)
    team_small = [Smallball() for i in range(10)]
    team_big = [Bigball() for i in range(10)]
    world += team_small
    world += team_big


running = True


def update_world(): # 객체들의 상호작용 시뮬레이션
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()


# initialization code
reset_world()

# game main loop code
running=True
while running:
    # game logic
    handle_events()
    update_world() #상호작용을 시뮬레이션
    render_world() #그 결과 보여준다.
    delay(0.05)


# finalization code

close_canvas()
