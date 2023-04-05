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

BG1 = pygame.transform.scale(pygame.image.load("background1.jpeg"), (WIDTH, HEIGHT))
sfbianco = pygame.transform.scale(pygame.image.load("sfondo_bianco.jpeg"), (WIDTH, HEIGHT))
fulmine = pygame.transform.scale(pygame.image.load("fulmine.jpeg"), (STAR_WIDTH+100, STAR_HEIGHT+100))
pannello = pygame.transform.scale(pygame.image.load("pannello.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
start = pygame.transform.scale(pygame.image.load("start.png"), (WIDTH, HEIGHT))


def draw(player, elapsed_time, stars ,point,stop, gamestarter):
    if gamestarter == True :
        WIN.blit(BG1, (0, 0))
        WIN.blit(pannello,(player.x,player.y))
        time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
        WIN.blit(time_text, (10, 10))
        point_text = FONT.render(f"Points: {round(point)}", 1, "white")
        WIN.blit(point_text, (WIDTH-150,10))
        for star in stars:
            WIN.blit(fulmine,(star.x,star.y))

    else:
        WIN.blit(start, (0,0))
        
            
    if elapsed_time > stop :
        WIN.blit(sfbianco, (0, 0))
        finish_text = FONT.render(f"Time expired, good job you have done {round(point)} points ", 1, "black")
        WIN.blit(finish_text, (0, 0))                
    if gamestarter == False :
        WIN.blit(start, (0,0)) 
        istruzioni = FONT.render(f" Premi Spacebar per iniziare a giocare", 30, "black")
        WIN.blit(istruzioni,(450,500 ))
    
    pygame.display.update() 


   
    

    







    


def main():
    gamestarter = False
    run = True
    vab = True
    stop = 10
    star_count=0
    point = 0
    start_time=0
    stars = []
    clock = new_func1() 
    player = new_func()
    star_add_increment= 2000
    start_time=0
    a=True
    
    

    while run:
        #Chiusura Gioco#
        for event in pygame.event.get():    
           if event.type == pygame.QUIT:
              run = False
                    
           else:
                run = True
        

        #Controllo del tempo
        if gamestarter == True and a==True :   
            start_time = new_func3() 
            a=False
        elapsed_time = time.time() - start_time
           


        #Stampa Stelle
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        if star_count > star_add_increment:
                for _ in range(3):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)                   
                

                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0
        
                
                
        #Tasto d'inizio         
        keys = new_func2()    
        if keys[pygame.K_SPACE] and vab == True :             
           gamestarter = True
           vab = False  
        
        
        
        
        

        #Gioco numero 1
        if  gamestarter == True and elapsed_time < stop:    
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT-50:
                    stars.remove(star)
                elif  star.colliderect(player) : 
                    stars.remove(star)
                    point=point+1
            keys = new_func2()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL



















        #Stampa del gioco
        draw(player, elapsed_time, stars, point,stop, gamestarter)

        

    pygame.quit()












def new_func5(star_x):
    star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
    return star

def new_func4():
    star_x = random.randint(0, WIDTH - STAR_WIDTH)
    return star_x

def new_func3():
    start_time=time.time()
    return start_time

def new_func2():
    keys = pygame.key.get_pressed()
    return keys

def new_func1():
    clock = pygame.time.Clock()
    return clock

def new_func():
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    return player





if __name__ == "__main__":
    main()





















 






    

