import pygame
import time
pygame.init()

WIDTH = 500
HEIGHT = 400

screen = pygame.display.set_mode([500,400])

jelly = pygame.image.load("jelly.png")

sky = pygame.image.load("sky.jpg")

jelly_x = 100
jelly_y = 10

#Only makes the key events true
keys = [False,False,False,False]


while jelly_y<400:
    screen.blit(sky,(0,0))
    screen.blit(jelly,(jelly_x,jelly_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:#Will check if the key is pressed
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_LEFT:
                keys[1] = True
            if event.key == pygame.K_DOWN:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP: #Checks if the key is released
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            if event.key == pygame.K_DOWN:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False
#0,1,2,3 are directions of the keys
    if keys[0]: #up
        if jelly_y>-100:
            jelly_y -= 10
    if keys[1]: #Left
        if jelly_x>0:
            jelly_x -= 10
    if keys[2]: #Down
        if jelly_y<400:
            jelly_y+=10
    if keys [3]: #Right
        if jelly_x<400:
            jelly_x+=10
    
    jelly_y += 5
    time.sleep(0.05)


print("Game Over")
    
