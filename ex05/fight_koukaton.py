import copy
import os
import pygame as pg
import random
import sys
import time


WINDOW_SIZE = (1600, 900) #ウインドウサイズ
LIFE_POINT = 3 #ライフ
INVINCIBLE_TIME = 1 #無敵時間(sec)
BOMB_NUM = 3 #爆弾の初期の数
ENEMY_NUM = 2 #敵キャラの数
HIT_STOP = 0.2 #ヒットストップの設定

class Screen(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pg.display.set_mode(WINDOW_SIZE)


class Image(Screen):
    def __init__(self, im_pass) -> None:
        """画像を扱うクラス

        Args:
            im_pass (string): 読み込む画像のパス
        """
        super().__init__()
        self.im_pass = im_pass
        self.image = pg.image.load(im_pass)
        self.rect = self.image.get_rect()
        
            
class Koukaton(Image):   
    key_dic = {
        "left":pg.K_LEFT, "right":pg.K_RIGHT, "up":pg.K_UP, 
        "down":pg.K_DOWN, "dash":pg.K_LSHIFT, "attack":pg.K_LCTRL,
        "exit":pg.K_ESCAPE, "reset":pg.K_F1
        } #キー の設定
    
    def __init__(self, im_pass, pos, speed=1) -> None:
        """こんかとんのクラス

        Args:
            pos (list): 初期座標
            speed (int, optional): こうかとんの移動速度. Defaults to 1.
        """
        super().__init__(im_pass)
        self.pos = pos
        self.speed = speed
        self.image = pg.transform.rotozoom(self.image, 0, 2.0)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.effct_image = pg.image.load("nc289332.png")
        self.effect_image = pg.transform.rotozoom(self.effct_image, 0, 0.6)
        self.effect_rect = self.effect_image.get_rect()
        self.attack_mode = False
        
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
        
        if pressed[Koukaton.key_dic["attack"]]:
            self.attack_mode = True     
            self.effect_rect.center = self.rect.center
            self.screen.blit(self.effect_image, self.effect_rect)
        elif pressed[Koukaton.key_dic["attack"]] == False:
            self.attack_mode = False
        
        #こうかとん が画面外に出たとき、元の位置に戻す、
        for i in range(2):
            # i == 0 のとき x座標が範囲外
            # i == 1 のとき y座標が範囲外
            if 0 >= self.rect[i] or self.rect[i] + self.rect[i+2]>= WINDOW_SIZE[i]:
                print(before_koukaton_rect)
                self.rect = before_koukaton_rect
        
    def change_image(self, ip):
        """画像を変更する

        Args:
            ip (string): 画像のパス
        """
        self.image = pg.image.load(ip)
        self.image = pg.transform.rotozoom(self.image, 0, 2.0)
            

class Enemy(Image):
    def __init__(self, im_pass, speed=[1, 1]) -> None:
        """敵のクラス

        Args:
            im_pass (string): 読み込む画像のパス
            speed (list, optional): [x方向の速度, y方向の速度]. Defaults to [1, 1].
        """
        super().__init__(im_pass)
        x = random.randint(0, WINDOW_SIZE[0])
        y = random.randint(0, WINDOW_SIZE[1])
        self.pos = [x, y]
        self.speed = speed
        self.image = pg.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.move_ip(self.speed)
        for i in range(2):
            # i == 0 のとき x 軸の計算
            # i == 1 のとき y 軸の計算
            #壁にぶつかったら反転
            if 0 >= self.rect[i] or self.rect[i] + self.rect[i+2] >= WINDOW_SIZE[i]:
                self.speed[i] *= -1

class BackGroundImage(Image):
    def __init__(self, im_pass,  title) -> None:
        """背景画像のクラス

        Args:
            im_pass (string): 読み込む画像のパス
            title (string): タイトル名
        """
        super().__init__(im_pass)    
        self.title = title
        pg.display.set_caption(self.title)
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
        
class Life(Image):
    def __init__(self, im_pass, pos, life=LIFE_POINT):
        """こうかとんのライフのクラス

        Args:
            im_pass (string): 読み込む画像のパス
            pos (tuple): 一つ目のライフの位置
            life (int, optional): 初期ライフの数. Defaults to LIFE_POINT.
        """
        super().__init__(im_pass)
        self.life = life
        self.pos = pos
        self.life_image = []
        self.life_rect = []
        for i in range(self.life):
            self.life_image.append(self.image)
            self.life_image[i] = pg.transform.rotozoom(self.life_image[i], 0, 0.3)
            self.life_rect.append(self.life_image[i].get_rect())
            self.life_rect[i].center = (self.pos[0] + i * 100, self.pos[1])
        
    def blit(self):
        for i in range(self.life):
            self.screen.blit(self.life_image[i], self.life_rect[i])


class Bomb(Image):
    def __init__(self, im_pass, speed=[1, 1]) -> None:
        """爆弾のクラス

        Args:
            im_pass (string): 読み込む画像のパス
            speed (list, optional): [x方向の速度, y方向の速度]. Defaults to [1, 1].
        """
        super().__init__(im_pass)
        x = random.randint(0, WINDOW_SIZE[0])
        y = random.randint(0, WINDOW_SIZE[1])
        self.pos = [x, y]
        self.speed = speed
        self.image = pg.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.rect.move_ip(self.speed)
        for i in range(2):
            # i == 0 のとき x 軸の計算
            # i == 1 のとき y 軸の計算
            #壁にぶつかったら反転
            if 0 >= self.rect[i] or self.rect[i] + self.rect[i+2] >= WINDOW_SIZE[i]:
                self.speed[i] *= -1
        
            
class Sound:
    def __init__(self, sd_name) -> None:
        """音のクラス

        Args:
            sd_name (string): 読み込むサウンドのファイル名
        """
        self.sd_name = sd_name
        pg.mixer.init(frequency = 44100)    # 初期設定
        self.music = pg.mixer.Sound(self.sd_name)     # 音楽ファイルの読み込み
        
        
class BGM(Sound):
    def __init__(self, sd_name) -> None:
        """BGMのクラス
        """
        super().__init__(sd_name)
        self.music.set_volume(0.1)
        self.music.play(-1)  # 音楽の再生回数(ループ再生)
        
    def stop_sound(self):
        self.music.stop()
        
class SoundEffect(Sound):
    def __init__(self, sd_name) -> None:
        """効果音のクラス
        """
        super().__init__(sd_name)
        self.music.set_volume(0.3)
        
    def start_sound(self):
        self.music.play(0)
        
    
        
#ゲームオーバー時の処理
def gameover():
    pg.quit()
    sys.exit()

#衝突時の処理
def collision_object(ko, lf, se):
    """
    爆弾とこうかとんの衝突時の処理

    Args:
        ko (Koukaton): こうかとん
        lf (Life): ライフ
        se (SoundEffect): 効果音
    """
    global crash_time
    time_end = time.time()
    #前回衝突時から今回衝突時の時間の差が無敵時間より大きいなら、ライフを減らす
    if time_end - crash_time < INVINCIBLE_TIME:
        return
    se.start_sound()
    #アタックモードならその後の処理はしない
    if ko.attack_mode:
        return
    if lf.life != 0:    
        time.sleep(HIT_STOP)
        crash_time = time.time()#衝突時の時間を保存する
        lf.life -= 1
        num = random.randint(0, 9)
        ko.change_image(f"../fig/{num}.png")
    #ライフが0 なら gameover()を実行
    if lf.life == 0:
        gameover()
            
    

def main():
    global crash_time
    os.chdir(os.path.dirname(__file__))
    print("pass:"+os.getcwd())
    pg.init()
    scr = Screen()
    clock = pg.time.Clock()    
    
    #BGMの設定
    bgm = BGM("こんとどぅふぇ素材No.0129-Last-Horizon.wav")
    
    #効果音の設定
    hit_enemy = SoundEffect(sd_name="nc172283.wav")
    hit_bomb = SoundEffect(sd_name="nc84862.wav")
    burn_sound = SoundEffect(sd_name="nc224596.wav")
    
    #背景の設定
    scr = BackGroundImage(im_pass="pg_bg.jpg" ,title="戦え、こうかとん")
    
    #こうかとん の設定
    koukaton = Koukaton(im_pass="../fig/0.png", pos=(900, 400))
    
    #こうかとん のライフ
    life = Life(im_pass="nc237709.png", pos=(200 ,100))
    
    #敵キャラの設定
    enemy = [Enemy(im_pass="nc223460.png") for i in range(ENEMY_NUM)]
    
    #爆弾の設定
    bomb = [Bomb("bakudan.png") for i in range(BOMB_NUM)]
    
    all_sprites = pg.sprite.Group() #画像の処理用
    bomb_sprites = pg.sprite.Group() #爆弾衝突判定用
    enemy_sprites = pg.sprite.Group() #敵キャラ衝突判定用
    
    all_sprites.add(scr, koukaton)
    for i in range(BOMB_NUM):
        all_sprites.add(bomb[i])
        bomb_sprites.add(bomb[i])
    for i in range(ENEMY_NUM):
        all_sprites.add(enemy[i])
        enemy_sprites.add(enemy[i])
    
    crash_time = time.time()
    
    while True:
        #画像の表示と更新
        all_sprites.draw(scr.screen)
        life.blit()
        
        #爆弾の衝突
        bomb_collided = pg.sprite.spritecollide(koukaton, bomb_sprites, True)
        if bomb_collided:
            collision_object(ko=koukaton, lf=life, se=hit_bomb)
        #敵キャラとの衝突
        enemy_collided = pg.sprite.spritecollide(koukaton, enemy_sprites, koukaton.attack_mode)
        if koukaton.attack_mode:
            se = burn_sound
        else:
            se = hit_enemy
        if enemy_collided:
            collision_object(ko=koukaton, lf=life, se=se)
        
        #キーの入力時の処理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            if event.type == pg.KEYDOWN:
                if event.key == Koukaton.key_dic["exit"]:
                    pg.quit()
                    sys.exit()
                if event.key == Koukaton.key_dic["reset"]:
                    crash_time = time.time()
                    bgm.stop_sound()
                    main()  
                
                print(f"push:{pg.key.name(event.key)}")  

        all_sprites.update()
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    main()
    