import pygame
import time
import random

pygame.font.init()
pygame.init()
infoObject = pygame.display.Info()

WIDTH =  infoObject.current_w 
HEIGHT =  infoObject.current_h- 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minigames")
elapsed_time=0

SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)    
GREEN = (0, 255, 0)    
RED = (255, 0, 0)    
BLACK= (0,0,0)   




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



def draw(player, elapsed_time, stars ,point,stop, gamestarter,ctr):
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
        finish_text = FONT.render(f"Time expired, good job you have scored {round(point)} points ", 1, "black")
        WIN.blit(finish_text, (0, 0)) 
        ctr= True
        
    if gamestarter == False :
        WIN.blit(start, (0,0)) 
        istruzioni = FONT.render(f" Premi Spacebar per iniziare a giocare", 30, "black")
        WIN.blit(istruzioni,(WIDTH/2-220,HEIGHT/2+15 ))
    pygame.display.flip()
     

def draw2(questions, current_question,gover,false_button,true_button,score):
    WIN.fill(SKY_BLUE)
    

    
    if gover == False and current_question<=10:
        pygame.draw.rect(WIN, RED, false_button)
        pygame.draw.rect(WIN, GREEN, true_button)
        true_text = FONT.render("Vero", True, BLACK)
        true_rect = true_text.get_rect(center=true_button.center)
        WIN.blit(true_text, true_rect)
        false_text = FONT.render("Falso", True, BLACK)
        false_rect = false_text.get_rect(center=false_button.center)
        WIN.blit(false_text, false_rect)
        pygame.draw.rect(WIN, SKY_BLUE, (0, 0, WIDTH, 150))  # Copre la domanda precedente con il colore dello sfondo
        question_text = FONT.render(questions[current_question], True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH//2, 100))    
        WIN.blit(question_text, question_rect)
        score_text = FONT.render(f"Punteggio {round(score)}  ", 1, "black")
        WIN.blit(score_text,(0,0))

    if gover == True :
        gameover_text = FONT.render("Game Over! Il tuo punteggio e': " + str(score), True, BLACK)
        gameover_rect = gameover_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        WIN.fill(RED)
        WIN.blit(gameover_text, gameover_rect)
        score_text = FONT.render("Punteggio: " + str(score), True, BLACK)
        score_rect = score_text.get_rect(center=(WIDTH//2, 400))
        WIN.blit(score_text, score_rect)


    pygame.display.update()
   
    

    







    


def gioco_1():
    ctr=False
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
    elapsed_time=0
    
    

    while run:
        
        
        keys = new_func2()
        
        #Chiusura Gioco#
        for event in pygame.event.get():    
           if event.type == pygame.QUIT :
              run = False
              
              pygame.quit()
              
              
           
           
        
        #print(ctr)
        #Controllo del tempo
        if gamestarter == True and a==True :   
            start_time=time.time() 
            a=False
        elapsed_time = time.time() - start_time
        #print(elapsed_time)
        if (elapsed_time>20 and gamestarter == True) or keys[pygame.K_ESCAPE]:
            pygame.time.delay(10)
            run= False
            return   


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
        
















        
        draw(player, elapsed_time, stars, point,stop, gamestarter,ctr)
    
        
        
def gioco_2(WIDTH,HEIGTH) : 

    







    running = True
    gover = False
    score = 0
    current_question = 0
    questions = ["Esistono pannelli fotovoltaici che funzionano anche di notte?", "Pannello fotovoltaico e solare sono la stessa cosa.", "Un pannello fotovoltaico dura in media 25 anni.", "Chi ha un panello fotovoltaico risparmia sulle bollette!", "NON esistono leggi che salvaguardino l'ambiente.","Il sole emette 5,2 x 10^24 Kilocalorie/Minuto?","L energia solare ci giunge sotto forma di onde acustiche","L energia solare ci giunge sotto forma di onde corte","Radiazione globale e sinonimo di radiazione effettiva","L albedo e il rapporto tra l energia riflessa e l energia totale in arrivo","L effetto serra non ce sempre stato","La cella di Hudley e in espansione?","L equatore termico corrisponde all equatore geografico"]
    correct_answers = [True, False, True, True, False,True,False,True,False,True,False,True,False]
    false_button = pygame.Rect(WIDTH*(2/3), 200, 100, 50)
    true_button = pygame.Rect(WIDTH*(1/3), 200, 100, 50)
    
    
    
    
    
    

    
    


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if true_button.collidepoint(event.pos):
                    if correct_answers[current_question]:
                        score+=1
                        current_question+=1
                    else:
                        score-=1
                        current_question+=1
                if false_button.collidepoint(event.pos):
                    if not correct_answers[current_question]:
                        score+=1
                        current_question+=1
                    else:
                        score-=1
                        current_question+=1
                
        if score<-3 :
            gover = True

        draw2(questions,current_question,gover,false_button,true_button,score)
        
        
        
            
            
    pygame.quit()    

        
  
    













def new_func5(star_x):
    star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
    return star

def new_func4():
    star_x = random.randint(0, WIDTH - STAR_WIDTH)
    return star_x



def new_func2():
    keys = pygame.key.get_pressed()
    return keys

def new_func1():
    clock = pygame.time.Clock()
    return clock

def new_func():
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    return player

   



    
    

    
   
   
       







def main(WIDTH,HEIGHT):
    
    gioco_1()
    gioco_2(WIDTH,HEIGHT)





if __name__ == "__main__":
    main(WIDTH,HEIGHT,)




















 






    

