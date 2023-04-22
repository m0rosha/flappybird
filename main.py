import pygame
from buttons import Button
win = pygame.display.set_mode((700,400))
pygame.display.set_caption('Flappy bird')
game = True 
fps = 60 
clock = pygame.time.Clock()
btn1 = Button(250,100,200,150,'pngwing.com.png')
btn2 = Button(250,200,200,150,'EXITBTN.PNG.png')

run = False



while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:

                run = not run 
    
    
  
    if run:
        win.fill((255,100,0))
    else:
        win.fill((0,0,0))
        if btn1.Draw(win):
            run = True
        if btn2.Draw(win):
            game = False
    
    pygame.display.update()
    clock.tick(fps)