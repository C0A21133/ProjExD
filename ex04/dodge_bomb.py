import pygame as pg
import sys
import os

WINDOW_SIZE = (1300, 600)

class Image:
    def __init__(self, im_pass, pos) -> None:
        self.im_pass = im_pass
        self.pos = pos
        

def main():
    os.chdir(os.path.dirname(__file__))
    print("pass:"+os.getcwd())
    pg.init()
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode(WINDOW_SIZE)
    screen = pg.display.get_surface()
    
    clock = pg.time.Clock()
    clock.tick(1000)
    
    bg_image = pg.image.load("pg_bg.jpg")
    rect_bg = bg_image.get_rect()
    
    koukaton = Image(im_pass="../fig/0.png", pos=(900, 400))
    koukaton_image = pg.image.load(koukaton.im_pass)
    koukaton_image = pg.transform.rotozoom(koukaton_image, 0, 2.0)
    koukaton_rect = koukaton_image.get_rect()
    koukaton_rect.center = koukaton.pos[0], koukaton.pos[1]
    
    
    while (1):
        pg.display.update()
        scrn_sfc.blit(bg_image, rect_bg)
        scrn_sfc.blit(koukaton_image, koukaton_rect)
        
        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:
            koukaton_rect.move_ip(-1, 0)
        if pressed[pg.K_RIGHT]:
            koukaton_rect.move_ip(1, 0)
        if pressed[pg.K_UP]:
            koukaton_rect.move_ip(0, -1)
        if pressed[pg.K_DOWN]:
            koukaton_rect.move_ip(0, 1)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                
                
                print(f"push:{pg.key.name(event.key)}")
        pg.display.update()
                    


if __name__ == "__main__":
    main()
    