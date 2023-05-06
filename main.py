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


gap_sizes = range(100, 200, 10)  
gap_size = random.choice(gap_sizes)

obstacle_widths = range(40, 80, 10)  
obstacle_heights = range(50, 200, 10)

screen_width = pygame.display.get_surface().get_width()
screen_height = pygame.display.get_surface().get_height()

top_height = random.randint(0, screen_height - gap_size)
bottom_height = screen_height - gap_size - top_height
 
top_obstacle = Obstacle(screen_width, 0, random.choice(obstacle_widths), top_height, towerpng)
bottom_obstacle = Obstacle(screen_width, top_height + gap_size, random.choice(obstacle_widths), bottom_height, towerpng)


top_height1 = random.randint(0, screen_height - gap_size) 
bottom_height1 = screen_height - gap_size - top_height1

  
top_obstacle1 = Obstacle(screen_width + 350, 0, random.choice(obstacle_widths), top_height1, towerpng)
bottom_obstacle1 = Obstacle(screen_width + 350, top_height1 + gap_size, random.choice(obstacle_widths), bottom_height1, towerpng)
sec_obs_list = [bottom_obstacle1, top_obstacle1]
first_obs_list = [top_obstacle, bottom_obstacle]

while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = not run 
        if run == True: 
            player.handle_events(e)
        
        
            
                
    
        
  
    if run:
        
        win.blit(bkgrnd_img,(0,0))
        
        player.draw(win)
        
        player.update()
        
        
        for obs in sec_obs_list:
         
            obs.draw(win)
            obs.update()
        for obss in first_obs_list:
             
            obss.draw(win)
            obss.update()   
            
        for el in first_obs_list:

            if player.rect.colliderect(el.rect):
                run = False 
        for el in sec_obs_list:
            if player.rect.colliderect(el.rect):
                run = False    
        
        
       
         

    else:
        
        if btn1.Draw(win):
            run = True
        if btn2.Draw(win):
            game = False
    
    pygame.display.update()
    clock.tick(fps)