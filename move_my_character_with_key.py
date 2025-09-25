from pico2d import *

def IDLE():
    frame = 0
    center_x = 400
    center_y = 300
    running = True
    while running:
        clear_canvas()
        grass.draw(400, 90)
        character.clip_draw(frame * 128, 1152, 128, 128, center_x, center_y, 128, 128)
        update_canvas()
        frame = (frame + 1) % 6
        for event in get_events():
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    running = False
                elif event.key == SDLK_LEFT:
                    center_x -= 10
                elif event.key == SDLK_RIGHT:
                    center_x += 10
                elif event.key == SDLK_UP:
                    center_y += 10
                elif event.key == SDLK_DOWN:
                    center_y -= 10
                # 화면 경계 체크
                center_x = max(0, min(center_x, 800))
                center_y = max(0, min(center_y, 600))

open_canvas()
character = load_image('SamuraiSheet.png')
grass = load_image('TUK_GROUND.png')

IDLE()

close_canvas()