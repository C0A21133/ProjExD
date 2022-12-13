import pygame as pg
import sys
import os

def main():
    os.chdir(os.path.dirname(__file__))
    print("pass"+os.getcwd())
    pg.init()
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    screen = pg.display.get_surface()
    
    clock = pg.time.Clock()
    clock.tick(1000)
    
    bg_image = pg.image.load("pg_bg.jpg")
    rect_bg = bg_image.get_rect()
    
    while (1):
        pg.display.update()
        scrn_sfc.blit(bg_image, rect_bg)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()


if __name__ == "__main__":
    main()
    