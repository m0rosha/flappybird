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


player = Plane(200,200,70,35,planepng)
obstacles = pygame.sprite.Group()
gap_size = 100
screen_width = pygame.display.get_surface().get_width()
screen_height = pygame.display.get_surface().get_height()

top_height = random.randint(0, screen_height - gap_size)
bottom_height = screen_height - gap_size - top_height
        
top_obstacle = Obstacle(screen_width, 0, 50, top_height,towerpng)
bottom_obstacle = Obstacle(screen_width, top_height + gap_size, 50, bottom_height,towerpng) 
  

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = not run 
        if run == True: 
            player.handle_events(e)
        
            
                
    if pygame.sprite.spritecollide(player, obstacles, False):
        run = False 
        
        
  
    if run:
        win.blit(bkgrnd_img,(0,0))
        
        player.draw(win)
        
        player.update()
        
        
        
        
        obstacles.add(top_obstacle)
        obstacles.add(bottom_obstacle)     
        obstacles.draw(win)
        obstacles.update()
            
        
        
        
       
         

    else:
        
        if btn1.Draw(win):
            run = True
        if btn2.Draw(win):
            game = False
    
    pygame.display.update()
    clock.tick(fps)