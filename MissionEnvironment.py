import pygame
import time
import random

# Initialize Pygame and its subsystems
pygame.font.init()
pygame.init()

# Get user screen dimensions and define game window
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h - 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mission Environment")

# Initialize variables
elapsed_time = 0
punteggio_tot = 0
SKY_BLUE, WHITE, GREEN, RED, BLACK = (135, 206, 235), (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)
FONT = pygame.font.SysFont("comicsans", 30)

# Player and star constants
PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL = 160, 180, 7
STAR_WIDTH, STAR_HEIGHT, STAR_VEL = 100, 90, 3

# Load images and scale them
image_folder = "Immagini/"
sfondo_no_omino = pygame.transform.scale(pygame.image.load(image_folder + "no_omino.jpg"), (WIDTH + 100, HEIGHT + 100))
sfbianco = pygame.transform.scale(pygame.image.load(image_folder + "sfondo_bianco.jpeg"), (WIDTH, HEIGHT))
fulmine = pygame.transform.scale(pygame.image.load(image_folder + "fulmine.jpeg"), (STAR_WIDTH + 100, STAR_HEIGHT + 100))
pannello = pygame.transform.scale(pygame.image.load(image_folder + "pannello.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
start = pygame.transform.scale(pygame.image.load(image_folder + "schermata_iniziale.jpg"), (WIDTH, HEIGHT))
sfondo_omino = pygame.transform.scale(pygame.image.load(image_folder + "con_omino.jpg"), (WIDTH, HEIGHT))
game_over = pygame.transform.scale(pygame.image.load(image_folder + "gameover.png"), (WIDTH, HEIGHT))
schermata_finale = pygame.transform.scale(pygame.image.load(image_folder + "fine_gioco.png"), (WIDTH, HEIGHT))

def draw(player, elapsed_time, stars, point, stop, gamestarter):
    if gamestarter:
        WIN.blit(sfondo_no_omino, (0, 0))
        WIN.blit(pannello, (player.x, player.y))
        WIN.blit(FONT.render(f"Tempo: {round(elapsed_time)}s", 1, WHITE), (10, 10))
        WIN.blit(FONT.render(f"Punti: {round(point)}", 1, WHITE), (WIDTH - 150, 10))
        for star in stars:
            WIN.blit(fulmine, (star.x, star.y))
    elif elapsed_time > stop:
        WIN.blit(sfondo_omino, (0, 0))
        WIN.blit(FONT.render(f"Ottimo lavoro, hai fatto {round(point)} punti!", 1, WHITE), (20, HEIGHT / 2 + 150))
    else:
        WIN.blit(start, (0, 0))
    pygame.display.flip()

def draw2(questions, current_question, gover, false_button, true_button, score, fine_gioco, punteggio_tot):
    WIN.fill(SKY_BLUE)
    if not gover and current_question < 11:
        pygame.draw.rect(WIN, RED, false_button)
        pygame.draw.rect(WIN, GREEN, true_button)
        WIN.blit(FONT.render("Vero", True, BLACK), FONT.render("Vero", True, BLACK).get_rect(center=true_button.center))
        WIN.blit(FONT.render("Falso", True, BLACK), FONT.render("Falso", True, BLACK).get_rect(center=false_button.center))
        WIN.blit(FONT.render(questions[current_question], True, BLACK), FONT.render(questions[current_question], True, BLACK).get_rect(center=(WIDTH // 2, 100)))
        WIN.blit(FONT.render(f"Punteggio {round(score)}", 1, BLACK), (0, 0))
    elif gover:
        WIN.blit(game_over, (0, 0))
    if fine_gioco:
        punteggio_tot += score
        WIN.blit(schermata_finale, (0, 0))
        WIN.blit(FONT.render(f"Punteggio totale: {round(punteggio_tot)}", 1, BLACK), (WIDTH / 2 - 75, HEIGHT / 2))
    pygame.display.update()

def gioco_1(punteggio_tot):
    elapsed_time, stop, point, star_count, star_add_increment = 0, 40, 0, 0, 2000
    a, gamestarter, vab, run = True, False, True, True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    stars = []
    clock = pygame.time.Clock()
    start_time = time.time()
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if gamestarter and a:
            start_time = time.time()
            a = False
        elapsed_time = time.time() - start_time

        if elapsed_time > stop + 15 or keys[pygame.K_ESCAPE]:
            pygame.time.delay(10)
            return

        star_count += clock.tick(60)
        if star_count > star_add_increment:
            stars.extend([pygame.Rect(random.randint(0, WIDTH - STAR_WIDTH), -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) for _ in range(3)])
            star_add_increment = max(1200, star_add_increment - 50)
            star_count = 0

        if keys[pygame.K_SPACE] and vab:
            gamestarter, vab = True, False

        if gamestarter and elapsed_time < stop:
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT - 50:
                    stars.remove(star)
                elif star.colliderect(player):
                    stars.remove(star)
                    point += 1
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL

        draw(player, elapsed_time, stars, point, stop, gamestarter)

def gioco_2(WIDTH, HEIGHT, punteggio_tot):
    running, gover, fine_gioco = True, False, False
    score, current_question = 0, 0
    questions = [
       "Esistono pannelli fotovoltaici che funzionano anche di notte", 
       "Pannello fotovoltaico e solare sono la stessa cosa", 
       "Un pannello fotovoltaico dura in media 25 anni.",
       "Il sole emette 5,2 x 10^24 Kilocalorie/Minuto",
       "L'energia solare ci giunge sotto forma di onde acustiche",
       "L'energia solare ci giunge sotto forma di onde corte",
       "Radiazione globale e' sinonimo di radiazione effettiva",
       "L'albedo e' il rapporto tra l'energia riflessa e l'energia totale in arrivo",
       "L'effetto serra c'e' sempre stato","La cella di Hudley e' in espansione",
       "L'equatore termico corrisponde all'equatore geografico"
        
    ]
    correct_answers = [True, False, True, True, False, True, False, True, True, True, False]
    false_button, true_button = pygame.Rect(WIDTH * (2 / 3), 200, 100, 50), pygame.Rect(WIDTH * (1 / 3), 200, 100, 50)

    while running:
        if not fine_gioco:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if true_button.collidepoint(event.pos):
                        if correct_answers[current_question]:
                            score += 1
                        else:
                            score -= 1
                        current_question += 1
                    if false_button.collidepoint(event.pos):
                        if not correct_answers[current_question]:
                            score += 1
                        else:
                            score -= 1
                        current_question += 1
        if score < -3:
            gover = True

        if current_question > 10:
            fine_gioco = True
        
        


        draw2(questions, current_question, gover, false_button, true_button, score, fine_gioco, punteggio_tot)
    pygame.quit()

def main(WIDTH, HEIGHT, punteggio_tot):
    gioco_1(punteggio_tot)
    gioco_2(WIDTH, HEIGHT, punteggio_tot)

if __name__ == "__main__":
    main(WIDTH, HEIGHT, punteggio_tot)

 






    

