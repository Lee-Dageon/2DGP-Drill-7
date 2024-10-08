from pico2d import *
from pygame.display import update


# Game object class here

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
    running = True


running = True


def update_world():
    pass
def render_world():
    clear_canvas()
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
