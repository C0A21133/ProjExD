import copy
import os
import pygame as pg
import random
import sys
import time


"""
ハートの画像 (nc237709.png)
https://commons.nicovideo.jp/material/nc237709

爆弾の画像 (bakudan.png)
https://www.irasutoya.com/2014/04/blog-post_4.html

BGM (こんとどぅふぇ素材No.0129-Last Horizon.wav)
https://conte-de-fees.com/bgm/2199.html
    
"""

WINDOW_SIZE = (1600, 900) #ウインドウサイズ
LIFE_POINT = 2 #ライフ
INVINCIBLE_TIME = 2 #無敵時間(sec)
BOMB_NUM = 1 #爆弾の初期の数
HIT_STOP = 0.2 #ヒットストップの設定

crash_time = 0

class Screen(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pg.display.set_mode(WINDOW_SIZE)


class Image(Screen):
    def __init__(self, im_pass) -> None:
        super().__init__()
        self.im_pass = im_pass
        self.image = pg.image.load(im_pass)
        self.rect = self.image.get_rect()
        
            
class Koukaton(Image):   
    key_dic = {
        "left":pg.K_LEFT, "right":pg.K_RIGHT, "up":pg.K_UP, 
        "down":pg.K_DOWN, "dash":pg.K_LSHIFT
        } #キー の設定
    
    def __init__(self, im_pass, pos, speed=1) -> None:
        super().__init__(im_pass)
        self.pos = pos
        self.speed = speed
        self.image = pg.transform.rotozoom(self.image, 0, 2.0)
        self.rect.center = self.pos
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        #こうかとん の移動の処理
        before_koukaton_rect = copy.deepcopy(self.rect) #こうかとん の移動前の座標
        pressed = pg.key.get_pressed()
        if pressed[Koukaton.key_dic["left"]]:
            self.rect.move_ip(-1 * self.speed, 0)
        if pressed[Koukaton.key_dic["right"]]:
            self.rect.move_ip(self.speed, 0)
        if pressed[Koukaton.key_dic["up"]]:
            self.rect.move_ip(0, -1 * self.speed)
        if pressed[Koukaton.key_dic["down"]]:
            self.rect.move_ip(0, self.speed)
            
        if pressed[Koukaton.key_dic["dash"]]:
            self.speed = 2
        elif pressed[Koukaton.key_dic["dash"]] == False:
            self.speed = 1
            
        #こうかとん が画面外に出たとき、元の位置に戻す、
        for i in range(2):
            # i == 0 のとき x座標が範囲外
            # i == 1 のとき y座標が範囲外
            if 0 >= self.rect[i] or self.rect[i]>= WINDOW_SIZE[i]:
                print(before_koukaton_rect)
                self.rect = before_koukaton_rect
        

class BackgroundImage(Image):
    def __init__(self, im_pass,  title) -> None:
        """_summary_

        Args:
            im_pass (string): _description_
            title (string): _description_
            size (tuple): _description_
        """
        super().__init__(im_pass)    
        self.title = title
        pg.display.set_caption(self.title)
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
        
class Life(Image):
    def __init__(self, im_pass, pos, life=LIFE_POINT):
        super().__init__(im_pass)
        self.life = life
        self.pos = pos
        self.life_image = []
        self.life_rect = []
        for i in range(self.life):
            self.life_image.append(self.image)
            self.life_image[i] = pg.transform.rotozoom(self.life_image[i], 0, 0.3)
            self.life_rect.append(self.rect)
            self.life_rect[i].center = (self.pos[0] + i * 100, self.pos[1])
        
    def blit(self):
        print(self.life_rect)
        for i in range(self.life):
            self.screen.blit(self.life_image[i], self.life_rect[i])


class Bomb(Image):
    def __init__(self, im_pass, speed=[2, 2]) -> None:
        super().__init__(im_pass)
        x = random.randint(0, WINDOW_SIZE[0])
        y = random.randint(0, WINDOW_SIZE[1])
        self.pos = [x, y]
        self.speed = speed
        self.image = pg.transform.rotozoom(self.image, 0, 0.3)
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.rect.move_ip(self.speed)
        for i in range(2):
            # i == 0 のとき x 軸の計算
            # i == 1 のとき y 軸の計算
            #壁にぶつかったら反転
            if 0 >= self.rect[i] or self.rect[i] >= WINDOW_SIZE[i]:
                self.speed[i] *= -1
            
class Sound:
    def __init__(self, sd_name) -> None:
        self.sd_name = sd_name
        pg.mixer.init(frequency = 44100)    # 初期設定
        pg.mixer.music.load(self.sd_name)     # 音楽ファイルの読み込み
        pg.mixer.music.play(-1)  # 音楽の再生回数(ループ再生)
        
        
#ゲームオーバー時の処理
def gameover():
    pg.quit()
    sys.exit()

#爆弾衝突時の処理
def check_bomb(ko, lf):
    """
    爆弾とこうかとんの衝突時の処理

    Args:
        ko (Koukaton): こうかとん
        lf (Life): ライフ
    """
    global crash_time
    time_end = time.time()
    
    #前回衝突時から今回衝突時の時間の差が無敵時間より大きいなら、ライフを減らす
    if time_end - crash_time < INVINCIBLE_TIME:
        return
    if lf.life != 0:
        time.sleep(HIT_STOP)
        crash_time = time.time()#衝突時の時間を保存する
        lf.life -= 1
        num = random.randint(0, 9)
        ko.im_pass = f"../fig/{num}.png"
    #ライフが0 なら gameover()を実行
    if lf.life == 0:
        gameover()
            

def main():
    os.chdir(os.path.dirname(__file__))
    print("pass:"+os.getcwd())
    pg.init()
    scr = Screen()
    clock = pg.time.Clock()    
    
    #BGMの設定
    bgm = Sound("こんとどぅふぇ素材No.0129-Last-Horizon.wav")
    
    #背景の設定
    scr = BackgroundImage(im_pass="pg_bg.jpg" ,title="戦え、効果トン")
    
    #こうかとん の設定
    koukaton = Koukaton(im_pass="../fig/0.png", pos=(900, 400))
    
    #こうかとん のライフ
    life = Life(im_pass="nc237709.png", pos=(200 ,300))
    
    bomb = Bomb("bakudan.png")
    
    all_sprites = pg.sprite.Group()
    all_sprites.add(scr, koukaton, bomb)
    koukaton_sprites = pg.sprite.Group()
    koukaton_sprites.add(koukaton)
    bomb_sprites = pg.sprite.Group()
    bomb_sprites.add(bomb)
    
    while True:
        #画像の表示と更新
        all_sprites.draw(scr.screen)
        all_sprites.update()
        
        #爆弾の衝突
        bomb_collided = pg.sprite.spritecollide(koukaton, bomb_sprites, False)
        if bomb_collided:
            check_bomb(ko=koukaton, lf=life)
        
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
    