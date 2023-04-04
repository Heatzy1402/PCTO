import pygame
import time
import random
pygame.font.init()
pygame.init()
infoObject = pygame.display.Info()

WIDTH = infoObject.current_w 
HEIGHT = infoObject.current_h- 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minigames")
#WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 100
PLAYER_VEL = 7
STAR_WIDTH = 80
STAR_HEIGHT = 70
STAR_VEL = 3
FONT = pygame.font.SysFont("comicsans", 30)

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
BG1 = pygame.transform.scale(pygame.image.load("bg1.jpeg"), (WIDTH, HEIGHT))
ful = pygame.transform.scale(pygame.image.load("ful1.jpeg"), (STAR_WIDTH+100, STAR_HEIGHT+100))
pan = pygame.transform.scale(pygame.image.load("pannello.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
st = pygame.transform.scale(pygame.image.load("start.jpeg"), (WIDTH, HEIGHT))





def draw(player, elapsed_time, stars,point,stop, gamestarter):
    if gamestarter == True :
        WIN.blit(BG, (0, 0))
        WIN.blit(pan,(player.x,player.y))
        time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
        WIN.blit(time_text, (10, 10))
        point_text = FONT.render(f"Points: {round(point)}", 1, "white")
        WIN.blit(point_text, (WIDTH-150,10))
    else:
        WIN.blit(st, (0,0))
    
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
    vab = True
    stop = 10
    star_add_increment = 2000
    point = 0
    star_count = 0
    start_time=0
    stars = []
    clock = new_func1() 
    player = new_func()
    
    
    
    
    

    while run:
        for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    run = False
                    
                else:
                    run = True
        keys = new_func2(player)    
        if keys[pygame.K_SPACE] and vab == True :         #Tasto per far partire il gioco    
            gamestarter = True
            vab = False  
            start_time = new_func3()
        elapsed_time = time.time() - start_time
        
        gioco_1(star_count,clock,gamestarter,elapsed_time,stop,stars,star_add_increment,player)
        draw(player, elapsed_time, stars, point,stop, gamestarter)

    pygame.quit()












def new_func5(star_x):
    star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
    #pygame.time.delay(250)
    return star

def new_func4():
    star_x = random.randint(0, WIDTH - STAR_WIDTH)
    return star_x

def new_func3():
    start_time=time.time()
    return start_time

def new_func2(player):
    keys = pygame.key.get_pressed()
    return keys

def new_func1():
    clock = pygame.time.Clock()
    return clock

def new_func():
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    return player

def gioco_1(star_count,clock,gamestarter,elapsed_time,stop,stars,star_add_increment,player):
    
    star_count += clock.tick(60)
    
        
    
    if  gamestarter == True and elapsed_time < stop:    
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT-50:
                    stars.remove(star)
                elif  star.colliderect(player) : #star.y + star.height >= player.y and
                    stars.remove(star)
                    point=point+1
                
                    break    #Meccanismo del gioco
            
            if star_count > star_add_increment:
                for _ in range(3):
                    star_x = new_func4()
                    star = new_func5(star_x)
                    stars.append(star)
                    
                    
                    

                star_add_increment = max(100, star_add_increment - 1)
                star_count = 0
            





            keys = new_func2(player)
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL




if __name__ == "__main__":
    main()
















 






    

