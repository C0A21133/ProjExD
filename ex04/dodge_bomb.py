import pygame as pg
import random
import sys
import copy
import os
import time

WINDOW_SIZE = (1600, 900) #ウインドウサイズ
LIFE_POINT = 3 #ライIN
INVINCIBLE_TIME = 1 #無敵時間(sec)
BOMB_NUM = 1 #爆弾の初期の数
HIT_STOP = 0.1 #ヒットストップの設定


class Image:
    def __init__(self, im_pass, pos) -> None:
        self.im_pass = im_pass
        self.pos = pos
        
class Koukaton(Image):
    def __init__(self, im_pass, pos, speed=1) -> None:
        super().__init__(im_pass, pos)
        self.speed = speed
        
class Life(Image):
    def __init__(self, im_pass, pos, life=LIFE_POINT):
        super().__init__(im_pass, pos)
        self.life = life

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
            

crash_time = 0

def gameover():
    pg.quit()
    sys.exit()

def check_bomb(ko, ko_rect, bb, lf):
    """_summary_

    Args:
        ko (Koukaton):
        ko_rect (Rect): _description_
        bb (Rect):
        lf (Life):
    """
    global crash_time
    time_end = time.time()
    
    #前回衝突時から今回衝突時の時間の差が無敵時間より大きいなら、ライフを減らす
    if time_end - crash_time < INVINCIBLE_TIME:
        return
    #ライフが0 なら gameover()を実行
    if ko_rect.colliderect(bb) == False:
        return
    else:
        
        if lf.life != 0:
            time.sleep(HIT_STOP)
            crash_time = time.time()#衝突時の時間を保存する
            lf.life -= 1
            num = random.randint(0, 9)
            ko.im_pass = f"../fig/{num}.png"
        if lf.life == 0:
            gameover()
            

def main():
    os.chdir(os.path.dirname(__file__))
    print("pass:"+os.getcwd())
    pg.init()
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode(WINDOW_SIZE)
    
    clock = pg.time.Clock()    
    
    #背景の設定
    bg_image = pg.image.load("pg_bg.jpg")
    rect_bg = bg_image.get_rect()
    
    #こうかとん の設定
    koukaton = Koukaton(im_pass="../fig/0.png", pos=(900, 400))
    koukaton_image = pg.image.load(koukaton.im_pass)
    koukaton_image = pg.transform.rotozoom(koukaton_image, 0, 2.0)
    koukaton_rect = koukaton_image.get_rect()
    koukaton_rect.center = koukaton.pos[0], koukaton.pos[1]
    #こうかとん のライフ
    life = Life(im_pass="nc237709.png", pos=(200 ,100))
    life_image = []
    life_rect = []
    for i in range(life.life):
        life_image.append(pg.image.load(life.im_pass))
        life_image[i] = pg.transform.rotozoom(life_image[i], 0, 0.3)
        life_rect.append(life_image[i].get_rect())
        life_rect[i].center = life.pos[0] + i * 100, life.pos[1]


    #爆弾の設定
    bomb = Bomb()
    
    while True:
        #こうかとん の画像の更新
        koukaton_image = pg.image.load(koukaton.im_pass)
        koukaton_image = pg.transform.rotozoom(koukaton_image, 0, 2.0)
        
        scrn_sfc.blit(bg_image, rect_bg)
        scrn_sfc.blit(koukaton_image, koukaton_rect)
        for i in range(life.life):
            scrn_sfc.blit(life_image[i], life_rect[i])
            
        bomb.move()
        bomb_circle = pg.draw.circle(scrn_sfc, (bomb.color), bomb.pos, bomb.rad)
        
        #こうかとん の移動の処理
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
            
        if pressed[pg.K_LSHIFT]:
            koukaton.speed = 2
        elif pressed[pg.K_LSHIFT] == False:
            koukaton.speed = 1
        
        #こうかとん が画面外に出たとき、元の位置に戻す、
        for i in range(2):
            # i == 0 のとき x座標が範囲外
            # i == 1 のとき y座標が範囲外
            if 0 >= koukaton_rect[i] or koukaton_rect[i] + koukaton_rect[2+i]>= WINDOW_SIZE[i]:
                print(before_koukaton_rect)
                koukaton_rect = before_koukaton_rect
        
        #爆弾の衝突
        check_bomb(ko=koukaton ,ko_rect=koukaton_rect, bb=bomb_circle, lf=life)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_F1:
                    main()
                print(f"push:{pg.key.name(event.key)}")
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    main()
    