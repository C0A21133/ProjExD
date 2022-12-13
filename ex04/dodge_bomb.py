import pygame as pg
import random
import sys
import copy
import os

WINDOW_SIZE = (1600, 900)

class Image:
    def __init__(self, im_pass, pos) -> None:
        self.im_pass = im_pass
        self.pos = pos
        
class Koukaton(Image):
    def __init__(self, im_pass, pos, speed=2) -> None:
        super().__init__(im_pass, pos)
        self.speed = speed

class Bomb:
    def __init__(self, rad= 10, color = "red", speed=[1, 1]) -> None:
        x = random.randint(0, WINDOW_SIZE[0])
        y = random.randint(0, WINDOW_SIZE[1])
        self.pos = [x, y]
        self.rad = rad
        self.color = color
        self.speed = speed
        
    def move(self):
        for i in range(2):
            # i == 0 のとき x 軸の計算
            # i == 1 のとき y 軸の計算
            self.pos[i] += self.speed[i]
            if 0 >= self.pos[i] or self.pos[i] + self.rad >= WINDOW_SIZE[i]:
                self.speed[i] *= -1
            

def main():
    os.chdir(os.path.dirname(__file__))
    print("pass:"+os.getcwd())
    pg.init()
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode(WINDOW_SIZE)
    screen = pg.display.get_surface()
    
    clock = pg.time.Clock()
    
    
    bg_image = pg.image.load("pg_bg.jpg")
    rect_bg = bg_image.get_rect()
    
    koukaton = Koukaton(im_pass="../fig/0.png", pos=(900, 400))
    koukaton_image = pg.image.load(koukaton.im_pass)
    koukaton_image = pg.transform.rotozoom(koukaton_image, 0, 2.0)
    koukaton_rect = koukaton_image.get_rect()
    koukaton_rect.center = koukaton.pos[0], koukaton.pos[1]

    bomb = Bomb()
    
    print(type(koukaton_rect))
    
    while (1):
        scrn_sfc.blit(bg_image, rect_bg)
        scrn_sfc.blit(koukaton_image, koukaton_rect)
        
        bomb.move()
        bomb_circle = pg.draw.circle(scrn_sfc, (bomb.color), bomb.pos, bomb.rad)
        
        before_koukaton_rect = copy.deepcopy(koukaton_rect) #こうかとん の移動前の座標
        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:
            koukaton_rect.move_ip(-1 * koukaton.speed, 0)
        if pressed[pg.K_RIGHT]:
            koukaton_rect.move_ip(koukaton.speed, 0)
        if pressed[pg.K_UP]:
            koukaton_rect.move_ip(0, -1 * koukaton.speed)
        if pressed[pg.K_DOWN]:
            koukaton_rect.move_ip(0, koukaton.speed)
        
        #こうかとん が画面外に出たとき、元の位置に戻す、
        for i in range(2):
            # i == 0 のとき x座標が範囲外
            # i == 1 のとき y座標が範囲外
            if 0 >= koukaton_rect[i] or koukaton_rect[i] + koukaton_rect[2+i]>= WINDOW_SIZE[i]:
                print(before_koukaton_rect)
                koukaton_rect = before_koukaton_rect
        
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
        clock.tick(1000)


if __name__ == "__main__":
    main()
    