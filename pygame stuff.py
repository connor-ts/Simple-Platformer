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
# im also kinda js banking on the fact that mac and windows have the same listing of fonts so its not a different font when ur on mac :sob:
font = pygame.font.SysFont(None, 36) # lets me search system fonts and use system fonts

# platforms
platforms = [
    pygame.Rect(300, 500, 200, 20),
    pygame.Rect(600, 400, 150, 20),     
    pygame.Rect(900, 300, 200, 20)         
]

# random variables 

groundY = 600
pgapx = (220, 350)
pgapy = (-120, 120)

# play stuffs lol
class Player:
    def __init__(self, x, y):
        ##size and pos
        self.rect = (x, y, 50, 50) 
        ##movement
        self.speed = 5
        self.velocity_xaxis = 0      # velocity x
        self.velocity_yaxis = 0      # velocity y
        self.jpower = -15       # how strong the jump is
        self.grav = 1    # normal gravity
        ###
        self.jpressed = False
        self.jcount = 0
        self.grounded = False  # checks if the player is standing on something, may help later with adding in features once the boilerplate is done
        
        ##dash
        self.dashing = False
        self.dash_s = 20 #dash speed
        self.dash_t = 10 #dash time
        self.dash_timer = 0 # dash timer /// not to be confused with time, time of dash is how long the physical dash is versus the timer which is in between 
        self.dash_c = 180 # time between dashes
        self.dash_cd_timer = 0 
        self.dash_p = False # checks if the Lshift is pressed /// held counts and will not allow dashing if Lshift is pressed again

    def movement(self, keys, platforms):
        # normal movement stuff
        move = 0
        if keys[pygame.K_a]: # key -> a
            move = -1
        if keys[pygame.K_d]: # key -> d
            move = 1
        if not self.dashing: # i think this is right, i mean it shouldnt break 
            pass # it should mean that when u dash when not moving itll like not move you 

## jumping func     
        if keys[pygame.K_SPACE] and not self.jpressed 
            if self.jcount < 2: # max of 2 jumps might change this later if i wanna make like fancy stuff with the jumping or like upgrades
                self.velocity_yaxis = self.jpower
                self.jcount += 1 # just adds one jump to the counter to keep track so that u dont jump more than 2 jumps
            self.jpressed = True
        if not keys[pygame.K_LSHIFT] # basically if the key aint pressed dont jump ;p
            self.jpressed = False

        if keys[pygame.K_LSHIFT] and not self.dash_p and self.dash_cd_timer <= 0:
            self.dashing = True 
            self.dash_timer = self.dash_t
            self.dash_cd_timer = self.dash_c
            self.velocity_yaxis = self.dash_speed if move >= 0 else -self.dash_speed # ai to figure this out because i thinky it looks weird that theres an if and else on the same line
            self.dash_p = True
        if not keys[pygame.K_LSHIFT]:
            self.dash_p = False

        if self.dashing

        


                

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

