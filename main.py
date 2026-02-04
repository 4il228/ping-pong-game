from pygame import *

window = window = display.set_mode((900, 800))

clock = time.Clock()
BG = "#b289ff"
game = True





while game:
    window.fill(BG)

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(60)

