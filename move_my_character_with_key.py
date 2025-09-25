from pico2d import *

def IDLE():
    frame = 0
    center_x = 400
    center_y = 300
    running = True
    while running:
        clear_canvas()
        character.clip_draw(frame * 128, 1152, 128, 128, center_x, center_y, 128, 128)
        update_canvas()
        frame = (frame + 1) % 6

open_canvas()
character = load_image('SamuraiSheet.png')

IDLE()

close_canvas()