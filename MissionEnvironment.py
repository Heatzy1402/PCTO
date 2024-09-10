import pygame
import time
import random

# Initialize Pygame modules
pygame.font.init()
pygame.init()

# Screen settings
info_object = pygame.display.Info()
WIDTH = info_object.current_w
HEIGHT = info_object.current_h - 100  # Adjust to leave space for window controls
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mission Environment")

# Colors
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont("comicsans", 30)

# Player settings
PLAYER_WIDTH = 160
PLAYER_HEIGHT = 180
PLAYER_VEL = 7

# Star (Falling Object) settings
STAR_WIDTH = 100
STAR_HEIGHT = 90
STAR_VEL = 3

# Asset folder
IMAGE_FOLDER = "Immagini/"

# Load and scale images, with error handling
def load_image(image_name, width=None, height=None):
    try:
        img = pygame.image.load(IMAGE_FOLDER + image_name)
        if width and height:
            img = pygame.transform.scale(img, (width, height))
        return img
    except pygame.error as e:
        print(f"Error loading image: {image_name} - {e}")
        pygame.quit()

# Load assets
background_no_player = load_image("no_omino.jpg", WIDTH+100, HEIGHT+100)
background_with_player = load_image("con_omino.jpg", WIDTH, HEIGHT)
background_white = load_image("sfondo_bianco.jpeg", WIDTH, HEIGHT)
lightning = load_image("fulmine.jpeg", STAR_WIDTH+100, STAR_HEIGHT+100)
panel = load_image("pannello.png", PLAYER_WIDTH, PLAYER_HEIGHT)
start_screen = load_image("schermata_iniziale.jpg", WIDTH, HEIGHT)
game_over_screen = load_image("gameover.png", WIDTH, HEIGHT)
final_screen = load_image("fine_gioco.png", WIDTH, HEIGHT)

# Draw the first game screen
def draw_first_game(player, elapsed_time, stars, points, stop_time, game_started):
    if game_started:
        WIN.blit(background_no_player, (0, 0))
        WIN.blit(panel, (player.x, player.y))
        time_text = FONT.render(f"Time: {round(elapsed_time)}s", True, WHITE)
        points_text = FONT.render(f"Points: {round(points)}", True, WHITE)
        WIN.blit(time_text, (10, 10))
        WIN.blit(points_text, (WIDTH - 150, 10))

        for star in stars:
            WIN.blit(lightning, (star.x, star.y))

    if elapsed_time > stop_time:
        WIN.blit(background_with_player, (0, 0))
        finish_text = FONT.render(f"Good job, you scored {round(points)} points!", True, WHITE)
        WIN.blit(finish_text, (20, HEIGHT//2 + 150))

    if not game_started:
        WIN.blit(start_screen, (0, 0))

    pygame.display.flip()

# Draw the second game screen
def draw_second_game(questions, current_question, game_over, false_button, true_button, score, game_finished, total_score):
    WIN.fill(SKY_BLUE)

    if not game_over and current_question < 11:
        pygame.draw.rect(WIN, RED, false_button)
        pygame.draw.rect(WIN, GREEN, true_button)
        
        true_text = FONT.render("True", True, BLACK)
        true_rect = true_text.get_rect(center=true_button.center)
        WIN.blit(true_text, true_rect)

        false_text = FONT.render("False", True, BLACK)
        false_rect = false_text.get_rect(center=false_button.center)
        WIN.blit(false_text, false_rect)

        question_text = FONT.render(questions[current_question], True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH // 2, 100))
        WIN.blit(question_text, question_rect)

        score_text = FONT.render(f"Score: {round(score)}", True, BLACK)
        WIN.blit(score_text, (0, 0))

    if game_over:
        WIN.blit(game_over_screen, (0, 0))

    if game_finished:
        total_score += score
        final_score_text = FONT.render(f"Total Score: {round(total_score)}", True, BLACK)
        WIN.blit(final_screen, (0, 0))
        WIN.blit(final_score_text, (WIDTH // 2 - 75, HEIGHT // 2))

    pygame.display.update()

# Function for the first game logic
def game_one(total_score):
    elapsed_time = 0
    game_started = False
    run = True
    player_movement_allowed = True
    stop_time = 40
    stars = []
    clock = pygame.time.Clock()
    player = create_player()
    star_add_increment = 2000
    points = 0
    star_counter = 0
    start_time = time.time()

    while run:
        keys = handle_input()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if game_started and player_movement_allowed:
            start_time = time.time()
            player_movement_allowed = False

        elapsed_time = time.time() - start_time

        if elapsed_time > stop_time + 15 or keys[pygame.K_ESCAPE]:
            run = False
            return

        star_counter += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_counter > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(1200, star_add_increment - 50)
            star_counter = 0

        if keys[pygame.K_SPACE] and player_movement_allowed:
            game_started = True
            player_movement_allowed = False

        if game_started and elapsed_time < stop_time:
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT - 50:
                    stars.remove(star)
                elif star.colliderect(player):
                    stars.remove(star)
                    points += 1
                    total_score = points

            move_player(keys, player)

        draw_first_game(player, elapsed_time, stars, points, stop_time, game_started)

# Function for the second game logic
def game_two(total_score):
    questions = [
        "Do solar panels work at night?",
        "Are photovoltaic and solar panels the same?",
        "Does a photovoltaic panel last around 25 years?",
        "Does the sun emit 5.2 x 10^24 Kilocalories/Minute?",
        # Add more questions as needed
    ]
    correct_answers = [True, False, True, True]
    game_finished = False
    running = True
    game_over = False
    score = 0
    current_question = 0

    false_button = pygame.Rect(WIDTH * (2 / 3), 200, 100, 50)
    true_button = pygame.Rect(WIDTH * (1 / 3), 200, 100, 50)

    while running:
        if not game_finished:
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
            game_over = True
        if current_question >= len(questions):
            game_finished = True

        draw_second_game(questions, current_question, game_over, false_button, true_button, score, game_finished, total_score)

    pygame.quit()

# Utility functions
def handle_input():
    return pygame.key.get_pressed()

def create_player():
    return pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

def move_player(keys, player):
    if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
        player.x -= PLAYER_VEL
    if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
        player.x += PLAYER_VEL

# Main game function
def main(total_score=0):
    game_one(total_score)
    game_two(total_score)

if __name__ == "__main__":
    main()

 






    

