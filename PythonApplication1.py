import pygame
import time
import random
pygame.font.init()
pygame.init()
infoObject = pygame.display.Info()
#ciao ciao ciao ciao ciao
WIDTH = infoObject.current_w 
HEIGHT = infoObject.current_h- 50
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minigames")
#WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
BG1 = pygame.transform.scale(pygame.image.load("bg1.jpeg"), (WIDTH, HEIGHT))
ful = pygame.transform.scale(pygame.image.load("ful1.jpeg"), (200, 200))
pan = pygame.transform.scale(pygame.image.load("pannello.png"), (200, 300))
st = pygame.transform.scale(pygame.image.load("start.jpeg"), (WIDTH, HEIGHT))
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 120
PLAYER_VEL = 5
STAR_WIDTH = 80
STAR_HEIGHT = 70
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time, stars,point,stop, gamestarter):
    WIN.blit(BG, (0, 0))
    WIN.blit(pan,(player.x,player.y))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    point_text = FONT.render(f"Points: {round(point)}", 1, "white")
    WIN.blit(point_text, (600,10))
    
    
    for star in stars:
        WIN.blit(ful, star)
    if elapsed_time > stop :
        WIN.blit(BG1, (0, 0))
        finish_text = FONT.render(f"Time expired, good job you have done {round(point)} points ", 1, "black")
        WIN.blit(finish_text, (0, 0))
    if gamestarter == False :
        WIN.blit(st, (0,0)) 
    pygame.display.update()    
    

    







    


def main():
    gamestarter = False
    run = True
    stop= 10
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    
    
    
    clock = pygame.time.Clock()
    
    point = 0
    vab = True 
    star_add_increment = 2000
    star_count = 0
    start_time=0
    stars = []

    while run:
        
        star_count += clock.tick(60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE] and vab == True :         #Tasto per far partire il gioco    
          gamestarter = True
          vab = False  
          start_time=time.time()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break                   #Tasto quit
        if  gamestarter == True and elapsed_time < stop:
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT-50:
                    stars.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player) :
                    stars.remove(star)
                    point=point+1
                
                    break    #Meccanismo del gioco
            
            if star_count > star_add_increment:
                for _ in range(3):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)                   
                    

                star_add_increment = max(100, star_add_increment - 1)
                star_count = 0
            





            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL
        elapsed_time = time.time() - start_time
        
            
            

           

        
        


        draw(player, elapsed_time, stars, point,stop, gamestarter)

    pygame.quit()


if __name__ == "__main__":
    main()
