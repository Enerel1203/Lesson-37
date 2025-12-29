import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play(-1)

font = pygame.font.SysFont(None, 36)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

choices = ["rock", "paper", "scissors"]
user_choice = None
computer_choice = None
result = ""

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                user_choice = "rock"
            elif event.key == pygame.K_p:
                user_choice = "paper"
            elif event.key == pygame.K_s:
                user_choice = "scissors"

            if user_choice:
                computer_choice = random.choice(choices)
                result = determine_winner(user_choice, computer_choice)

    title = font.render("Press R (Rock), P (Paper), S (Scissors)", True, (255, 255, 255))
    screen.blit(title, (50, 40))

    if user_choice:
        text1 = font.render(f"You chose: {user_choice}", True, (255, 255, 255))
        text2 = font.render(f"Computer chose: {computer_choice}", True, (255, 255, 255))
        text3 = font.render(result, True, (255, 255, 0))

        screen.blit(text1, (50, 120))
        screen.blit(text2, (50, 160))
        screen.blit(text3, (50, 200))

    pygame.display.update()

pygame.quit()
sys.exit()
