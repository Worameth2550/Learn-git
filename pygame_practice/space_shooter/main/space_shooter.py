import pygame
from os.path import join
from random import randint, uniform

class Player(pygame.sprite.Sprite):#pygame.sprite.Sprite ใช้เพื่อเก็บข้อมูลภาพ และ ตำแหน่ง
    def __init__(self,group):#ใช้สืบทอดและทำเป็น group sprite
        super().__init__(group)
        self.original_surf = pygame.image.load(join('Python','pygame_practice','space_shooter','main','..','images','player.png')).convert_alpha()
        self.image = self.original_surf
        self.rect =  self.image.get_frect(center=(window_width/2,window_height/2))
        self.direction = pygame.Vector2()#ค่าคือ(0,0)
        self.speed = 300

        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration =400  

    

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:#เอาlaer shoot time มาลบเพื่อให้ได้ค่ามากกว่าcooldown ที่กำหนด
                self.can_shoot = True

    def update(self,dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        self.rect.clamp_ip(display_surface.get_rect())
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop , (all_sprites,laser_sprite))
            laser_sound.play()
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()#จะเก็บค่าเวลาที่ใช้ัรนไปเรื่อยๆจะอัพเดทเป็นเลขล่าสุดตอนกดยิงของ current time

        self.laser_timer()

        

class star(pygame.sprite.Sprite):
    def __init__(self, groups,surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center=(randint(0,window_width),randint(0,window_height)))
   
class Laser(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos )

    def update(self,dt):
        self.rect.centery -= 400*dt
        if self.rect.bottom < 0 :
            self.kill()

class meteor(pygame.sprite.Sprite):
        def __init__(self,surf,pos,groups):
            super().__init__(groups)
            self.image= surf
            self.rect = self.image.get_frect(center = pos)
            self.star_time = pygame.time.get_ticks()
            self.lifetime = 3000
            self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
            self.speed = randint(400,700)
            self.meteor_surface = surf
            self.rotation = 0

        def update(self,dt):
            self.rect.center += self.direction * self.speed *dt
            self.rotation += randint(40,80) *dt
            self.image = pygame.transform.rotate(self.meteor_surface, self.rotation )
            self.rect = self.image.get_frect(center = self.rect.center)
            if pygame.time.get_ticks() - self.star_time >= self.lifetime:
                self.kill()

def collision() :
    global running
    
    collision_sprites = (pygame.sprite.spritecollide(player , meteor_sprite,True, pygame.sprite.collide_mask)) #spritecollide คือตัว meteor เมื่อชนกับ player meteor จะหายไป
    if collision_sprites:
        running = False

    for laser in laser_sprite :
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprite ,True)
        if collided_sprites:
            laser.kill()
            animatedexplosion(explosion_frames,laser.rect.midtop,all_sprites)
            explosion_sound.play()

def display_score():
    current_time=pygame.time.get_ticks() // 100
    text_surface = font.render(str(current_time), True , (240,240,240))
    text_rect = text_surface.get_frect(midbottom = (window_width/2,window_height - 50))
    display_surface.blit(text_surface,text_rect)
    pygame.draw.rect(display_surface,'white',text_rect.inflate(20,10).move(0,-8),5,10)

class animatedexplosion(pygame.sprite.Sprite):
    def __init__(self,frames,pos, groups):
        super().__init__(groups)
        self.frame = frames
        self.frame_index = 0
        self.image = self.frame[self.frame_index]
        self.rect= self.image.get_frect(center = pos)

    def update(self, dt):
        self.frame_index += 20 * dt
        if self.frame_index < len(self.frame):
            self.image = self.frame[int(self.frame_index)] 
        else: 
            self.kill()



#general setup
pygame.init()
window_width , window_height= 1280,720
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

#import
star_surface = pygame.image.load(join('Python','pygame_practice','space_shooter','main','..','images','star.png')).convert_alpha()
meteor_surf =pygame.image.load(join('Python','pygame_practice','space_shooter','main','..','images','meteor.png')).convert_alpha()
laser_surf=pygame.image.load(join('Python','pygame_practice','space_shooter','main','..','images','laser.png')).convert_alpha()
font = pygame.font.Font(join('Python','pygame_practice','space_shooter','main','..','images','Oxanium-Bold.ttf') , 50) #(font,size)
explosion_frames = [pygame.image.load(join('Python','pygame_practice','space_shooter','main','..','images','explosion',f'{i}.png')).convert_alpha() for i in range(21)]
#sound
laser_sound = pygame.mixer.Sound(join('Python','pygame_practice','space_shooter','main','..','audio','laser.wav'))
laser_sound.set_volume(0.5)
explosion_sound = pygame.mixer.Sound(join('Python','pygame_practice','space_shooter','main','..','audio','explosion.wav'))
game_music = pygame.mixer.Sound(join('Python','pygame_practice','space_shooter','main','..','audio','game_music.wav'))
game_music.set_volume(0.4)
game_music.play(loops=running)
#sprite
all_sprites = pygame.sprite.Group() #เป็นการจัดกลุ่มทุก class ให้อยู่กลุ่มใหญ่ที่สุดคือ all_sprite เมื่อรันคำสั่งจากตัวแปรนี้จะทำให้classที่ถูกเพิ่มเข้าไปทำงานพร้อมกัน
meteor_sprite = pygame.sprite.Group()
laser_sprite = pygame.sprite.Group()
for i in range (30):
    star(all_sprites,star_surface) # star_surfaceให้เป็นตัวโหลดภาพแทนเพราะหากใส่ในclassจะทำให้เครื่องต้องรันภาพทับกันทั้งภาพถึง 20 ภาพแต่หากสร้างตัวแปรจะโหลดแค่ภาพดาว
player = Player(all_sprites)


#custom evevts -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


while running:
    dt=clock.tick()/1000 #setting frame rate
    # event loop / set up เบื้องต้น
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # .quit ใช้เพื่อยับยั้งการรันโค้ดอันอื่นๆ กับ .QUIT ใช้เพื่อให้หยุดทำงานหากมีคำสั่งที่ต่างจากปกติ (มีเฉพาะใน pygame)
            running=False
        if event.type == meteor_event:
            x , y = randint(0,window_width),randint(-200,-100)
            meteor(meteor_surf, (x,y),(all_sprites,meteor_sprite))#เขียนลำดับตามparameterให้ถูกต้องในclass meteorเขียนparameter เป็น group surf posซึ่งมันจะเก็บค่าจรงตามตัวแปรที่เขียนเป็นลำดับของช่องนี้
    # update surface
    all_sprites.update(dt)
    collision()
    #draw the game
    display_surface.fill('#3a2e3f') 
    all_sprites.draw(display_surface)
    display_score()
    #draw test
   

    pygame.display.update()

pygame.quit()

