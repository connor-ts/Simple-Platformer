# connor ter stege
# 13th of jan
# scuffed platformer game in pygame

## Uses of ai ->
## I personally wouldnt say im fluent in python as its not my main language so some 
## LLM and google searches will be used to find out how to solve errors as my main goal 
## is just to make a working game that i like rather than doing something thats not fully what i wanted but 100% me

# things i plan to add, sprite thing with a cat image
# maybe double jump
# dashing maybe, because thats quite hard to do

import pygame
import random
import sys # i might remove this later because its only really helpful in my eyes to windows 11

pygame.init()

# meow meow cat stuff because i think the sprite is more fire lol
cat = image.load('cat.png')
cat = transform.scale(cat, (50, 50))

# setup stuffs
screen = pygame.display.set_mode((1280, 720)) # i dont remember the actual res of the screens at 
# school but i dont want to make them too large or small so i assume that 720p reso- is enough :p
pygame.display.set_caption("simple platformer") # i might think of a name later, but honestly this good lwk
clock = pygame.time.Clock()

# fonts if i add more later maybe
font1 = pygame.font.SysFont(None, 48) # lots of info from here especially for sys stuff: https://www.pygame.org/docs/ref/font.html

# game state variable
state = "menu"

# start button drawing
start = pygame.Rect(1280 // 2 - 100, 720 // 2 - 40, 200, 80) 

# color palette
Background = (130, 184, 189) # just used google to search up rgb for a light blue
White = (255, 255, 255) ## same here
Green = (55, 163, 84) ## same here

# cube/player
class cube:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.y_velocity = 0 
        self.speed = 7 # speed of the cube
        self.jumpstrength = -15 # might make this lower or higher depending on how easy it is
        self.onground = False # ground variable checks if it was
    def movement(self, platforms, keyboard):
        if keyboard[pygame.K_a]:
            self.rect.x -= self.speed
            for x in platforms:
                if self.rect.colliderect(x): # the info i found on colliderect was found mostly this pygame doc: https://www.pygame.org/docs/ref/rect.html
                    self.rect.left = x.right
        if keyboard[pygame.K_d]:
            self.rect.x += self.speed
            for x in platforms:
                if self.rect.colliderect(x): ## same here https://www.pygame.org/docs/ref/rect.html
                    self.rect.right = x.left  
        if keyboard[pygame.K_SPACE] and self.onground: # controls jumping using space bar
            self.y_velocity = self.jumpstrength
            self.onground = False   # stops inf jumping when ur in the sky
        self.y_velocity += 1 # gravity logic so that the cube comes down after u press space, this was a pain
        if self.y_velocity > 20: # terminal velocity cap, because somehow it was causing issues with the collision 
            self.y_velocity = 20 ## not a lot but some helpful advice was found: https://www.pygame.org/docs/ref/math.html // but mostly on google
        self.rect.y += self.y_velocity

### LLM was used to fix
        # Collision detection
        self.onground = False
        for p in platforms:
            if self.rect.colliderect(p):
                if self.y_velocity >= 0:  # falling down
                    self.rect.bottom = p.top
                    self.y_velocity = 0
                    self.onground = True
                elif self.y_velocity < 0:  # moving up (hit head)
                    self.rect.top = p.bottom
                    self.y_velocity = 0
### end
## explaination:
# i was having lots of issues keeping the platforms collidable and non collidable, 
# all this code basically supports is it arranges the logic of the cube and platforms to where when the cube
# touches another rectangle as the background isnt a rectangle it can stand, touch, etc on top of the rectangle
## ive intentionally left the ai comments so u can see the difference between the code.

screen.blit(cat, (x, y))

# objects
player = cube(200, 500) # cube dimensions
platforms = [pygame.Rect(150, 550, 220, 20)] # dimensions of the generating platforms
score = 0 # score tracker
xcam = 0 # basically just how far right to move the camera when follwoing the cube
dead = 720 + 50 # just means if u go too low it breaks and resets u

# game loop
playing = True

while playing:
    clock.tick(60) # fps
    screen.fill(Background) # gives the game a background obv 
    
    for event in pygame.event.get():    # we did this in class
        if event.type == pygame.QUIT:   # and it was also in the mario game example
            playing = False
        
        if state == "menu" and event.type == pygame.MOUSEBUTTONDOWN: # lets me make a play button that works when you click it
            if start.collidepoint(event.pos):                        # lots of info was found on google, using llms and this specific
                state = "gaming"                                     # pygame doc: https://www.pygame.org/docs/ref/mouse.html

    if state == "menu": 
        pygame.draw.rect(screen, Green, start) # draws the green rectangle that will have our play button in it
        text = font1.render("play", True, White)
        screen.blit(text, text.get_rect(center=start.center)) # google helped me figure out how to center it
    else:
        keyboard = pygame.key.get_pressed()
        player.movement(platforms, keyboard)
        xcam = player.rect.x - 200 # so the camera is slightly offset so it easier to follow the player instead of being in the exact middle
                                   # also an example would be if the player is at 500, the cam would be at 300 because the xcam runs this 500-200=x 
                                   # to figure out where to position itself and it does this until reset or the games is closed

### LLM used to fix
        # Generate platforms ahead
        farthest_x = max(p.right for p in platforms)
        while farthest_x < player.rect.x + 1280:
            gap_x = random.randint(120, 180)
            gap_y = random.randint(-50, 50)
            prev_y = platforms[-1].y
            new_y = max(100, min(720 - 50, prev_y + gap_y))
            new_platform = pygame.Rect(farthest_x + gap_x, new_y, 200, 20)
            platforms.append(new_platform)
            farthest_x = new_platform.right

        # Remove old platforms behind player
        platforms = [p for p in platforms if p.right > player.rect.x - 200]

        # Draw platforms
        for p in platforms:
            pygame.draw.rect(screen, Green, (p.x - xcam, p.y, p.width, p.height))
### end
## explaination
# same as last time where i couldnt find a perfect way to make the platforms generate as i went ahead,
# used an LLM to make the code and save me the time from doing endless research as id already poured 2 hours on this one section
# i also couldnt figure out what components to use fully and where, and stated earlier 
# id rather have a game that works and i like rather than one that runs off hopes and dreams

        player.draw(xcam) # drawing the camera for the player
       
        score = max(score, player.rect.x) # keeps score 
        score_text = font1.render(f"Score: {score}", True, White) # font and color from: https://www.pygame.org/docs/ref/font.html
        screen.blit(score_text, (10, 10)) # quick google search helped me figure out how blit works as i didnt fully understand from: https://www.pygame.org/docs/ref/surface.html

        if player.rect.top > dead: # this basically just resets u instead of killing the window, it also made it easier to test, 
            player.rect.x = 200    # more complex, it kills everything, generates the cube again, and puts the player and camera back at the start,
            player.rect.y = 500    # this also resets the score
            player.y_velocity = 0
            player.onground = False
            platforms = [pygame.Rect(150, 550, 220, 20)]
            score = 0
            xcam = 0

    pygame.display.flip() # keeps the display goin

pygame.quit()
sys.exit() # ive used no sys in the past and had memory leaks, obviously this isnt using a lot of ram but i still like to have it there from,
           # half from habit and also it helps with other things

