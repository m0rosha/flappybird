import pygame
import random 
from buttons import Button
from sprite import Plane
from towers import Obstacle 
win = pygame.display.set_mode((700,400))
pygame.display.set_caption('Flappy bird 9/11')
game = True 
fps = 60 
towerpng = 'Tower.png'
planepng = 'Airplane.png'
skyimg = 'Sky.jpg'

clock = pygame.time.Clock()

btn1 = Button(250,100,200,150,'pngwing.com.png')
btn2 = Button(250,200,200,150,'EXITBTN.PNG.png')

run = False
bkgrnd = pygame.image.load(skyimg)
bkgrnd_img = pygame.transform.scale(bkgrnd,(700,400))
#def make_top_tower():



player = Plane(200,200,70,35,planepng)
obstacles = pygame.sprite.Group()
gap_size = 100
screen_width = pygame.display.get_surface().get_width()
screen_height = pygame.display.get_surface().get_height()

top_height1 = random.randint(0, screen_height - gap_size)
top_height2 = random.randint(0, screen_height - gap_size)
top_height3 = random.randint(0, screen_height - gap_size)
top_height4 = random.randint(0, screen_height - gap_size)
bottom_height1 = screen_height - gap_size - top_height1
bottom_height2 = screen_height - gap_size - top_height2
bottom_height3 = screen_height - gap_size - top_height3
bottom_height4 = screen_height - gap_size - top_height4     
top_obstacle1 = Obstacle(screen_width, 0, 50, random.randint(0, screen_height - gap_size),towerpng)
top_obstacle2 = Obstacle(screen_width+300, 0, 50, random.randint(0, screen_height - gap_size),towerpng)
top_obstacle3 = Obstacle(screen_width+300, 0, 50, random.randint(0, screen_height - gap_size),towerpng)
top_obstacle4 = Obstacle(screen_width+300, 0, 50, random.randint(0, screen_height - gap_size),towerpng)

bottom_obstacle1  = Obstacle(screen_width, (screen_height - gap_size - top_height1) + gap_size, 50, bottom_height1,towerpng) 
bottom_obstacle2 = Obstacle(screen_width+300, (screen_height - gap_size - top_height2) + gap_size, 50, bottom_height2,towerpng) 
bottom_obstacle3 = Obstacle(screen_width+300, (screen_height - gap_size - top_height3) + gap_size, 50, bottom_height3,towerpng) 
bottom_obstacle4 = Obstacle(screen_width+300, (screen_height - gap_size - top_height4) + gap_size, 50, bottom_height4,towerpng) 
  
bot_obs_list = [bottom_obstacle1,bottom_obstacle2,bottom_obstacle3,bottom_obstacle4]
top_obs_list = [top_obstacle1,top_obstacle2,top_obstacle3,top_obstacle4]


while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = not run 
        if run == True: 
            player.handle_events(e)
        
            
                
    if player.rect.x and player.rect.y == bot_obs_list:
        run = False 
        
        
  
    if run:
        win.blit(bkgrnd_img,(0,0))
        
        player.draw(win)
        
        player.update()
        
        
        for obs in bot_obs_list:
            obs.draw(win)
            obs.update()
        for obss in top_obs_list:
            obss.draw(win)
            obss.update()   
        
        
        
       
         

    else:
        
        if btn1.Draw(win):
            run = True
        if btn2.Draw(win):
            game = False
    
    pygame.display.update()
    clock.tick(fps)