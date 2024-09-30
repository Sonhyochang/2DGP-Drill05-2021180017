from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('pra2.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2

def handle_events():
    global running,dir
    global dir2


    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -=1
            elif event.key == SDLK_DOWN:
                dir2 +=1

def move_dir():
    if dir == 0 and dir2 == 0:
        character.clip_draw((frame * 460), 1800, 460, 600, x, y, 75, 75)
    elif dir > 0 :
        character.clip_draw((frame * 460), 1200, 460, 600, x, y, 75, 75)
    elif dir < 0:
        character.clip_composite_draw((frame*460),1200,460,600,0,'h',x,y,75,75)
    elif dir2 > 0:
        character.clip_draw((frame * 460), 0, 460, 600, x, y, 75, 75)
    elif dir2 < 0:
        character.clip_draw((frame * 460), 1800, 460, 600, x, y, 75, 75)

def move_limit():
    global x,y
    if TUK_WIDTH > x > 0:
        x += dir * 10
        y += dir2 * 10
    elif x>=TUK_WIDTH:
        x= x-10
        y += dir2 * 10
    elif x<=0:
        x=x+10
        y += dir2 * 10
    elif TUK_HEIGHT > y > 0:
        x += dir * 10
        y += dir2 * 10
    elif y>=TUK_HEIGHT:
        x += dir * 10
        y=y-10
    elif y<=0:
        x += dir * 10
        y=y+10

frame = 0
dir = 0
dir2 = 0

while running:
    clear_canvas()
    background.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    move_dir()
    update_canvas()
    handle_events()
    frame = (frame +1) % 4
    move_limit()
    delay(0.05)



close_canvas()

