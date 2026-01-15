# connor ter stege
# uhhh today is the 13th of jan
# platformer game in pygame
# ai might be used to save time on repeat tasks or unknown errors, if i didnt use it ill remove this.. nuless i forget :p
## i barely comment on my personal code so this is probably gonna be littered with comments of what things do, ill try to avoid obvious ones
## my common variable uses are the first letters and last letters of the alphabet unless its specifically named -> a,b,c,x,y,z

import pygame, random, os # used os possibly because coding on both mac and windows and certain commands can help make sure code still works on both versions :)
import sys # helps close the active window faster and easier on windows, probably will remove after final push
pygame.init()

### screen /// setup
screen = pygame.display.set_mode((1280, 720)) # 720p reso
pygame.display.set_caption("low quality platformer")
clock = pygame.time.Clock()

# platforms
platforms = [
    (300, 500, 200, 20),
    (600, 400, 150, 20),     
    (900, 300, 200, 20)         
]

# play stuffs lol
class Player:
    def __init__(self, x, y):
        ##size and pos
        self.width = 50 
        self.height = 50
        self.x = x          
        self.y = y   
        ##movement
        self.speed = 5
        self.velocity_xaxis = 0      # velocity x
        self.velocity_yaxis = 0      # velocity y
        self.jpower = -15       # how strong the jump is
        self.grav = 1        # normal gravity
        self.grounded = True  # checks if the player is standing on something, may help later with adding in features once the boilerplate is done
        ##dash
        self.dash_s = 20 #dash speed
        self.dash_t = 10 #dash time
        self.dash_c = 0 #counter for dash timer
        self.dashing = False

    def movement(self, keys, platforms):
        # normal movement stuff
        move_dir = 0
        if keys[pygame.K_a]: # key -> a
                move_dir = -1
        if keys[pygame.K_d]: # key -> d
                move_dir = 1
        if not self.dashing:
            self.x += move_dir * self.speed

## jumping func     
        if keys[pygame.K_SPACE] and self.grounded: # makes it so u cant jump when ur in the sky bc this aint flappy bird 
            self.velocity_yaxis = self.jpower
            self.grounded = False # indicates player is not on ground
        #application of gravity
        self.velocity_yaxis += self.grav 
        self.y += self.velocity_yaxis
        #platform collision 
        ## ai code was created to understand the logic of the player and platforms colliding
        ### this is NOT the code generated but similar to the practice code
        for pm in platforms:
            px, py, pw, ph = pm # px -> platform x axis /// py -> platform y axis /// pw -> platform width /// ph -> platform height    
            if self.velocity_yaxis >=0 and self.x +self.width > px and self.x < px + pw:
                # logic to tell the player that they are on ground when touching a platform
                ## which allows them to jump again and dash again
                if self.y + self.height >= py and self.y + self.height <= py + ph:
                    self.y = py - self.height
                    self.velocity_yaxis = 0
                    self.grounded = True
        #application of floor collision
        if self.y >= 600: # ground 
            self.y = 600
            self.velocity_yaxis = 0
            self.grounded = True

## dash func
        if keys[pygame.K_LSHIFT] and not self.dashing: # does a burst in movement when hitting left shift
            self.dashing = True
            self.dash_c = self.dash_t
                #application of horizontal movement
            if keys[pygame.K_a]:
                self.velocity_xaxis = -self.dash_s
            elif keys [pygame.K_d]:
                self.velocity_xaxis = self.dash_s
            else:
                pass

        if self.dashing:
            self.x += self.velocity_xaxis
            self.dash_c -= 1
            if self.dash_c <= 0:
                self.dashing = False
                self.velocity_xaxis = 0

# testing features and stuff here
    def draw(self, screen):
       pygame.draw.rect(screen, (255, 255, 255), (
        self.x,
        self.y, 
        self.width, 
        self.height))

player = Player(100, 600)

# game loop
playing = True
while playing: # simple loop to keep the window running
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            playing = False

    keys = pygame.key.get_pressed()
    player.movement(keys, platforms)

# background, contant screen update
    screen.fill((30, 30, 40))
    for a in platforms:
        pygame.draw.rect(screen, (100, 200, 100), a)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

### more info on sys because i feel i wasnt clear enough to mac users lol, uhh basically theres these things called 
### memory leaks which programs like discord and often chat messengers and game development softwares like unity and roblox studio are notorious for constantly using 
### memory until it spikes to 100% and crashing the program or your pc, knowing how windows 11 is poorly coded in some aspects, without sys.exit sometimes ill close a pygame window 
### but windows wont actually close it until you end task in task manager  
