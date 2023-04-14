
import pygame
import time
import random
 
snake_speed = 15
 
# taille de la fenêtre
window_x = 720
window_y = 480
 
#variable des couleurs
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
#Initialisé Pygame
pygame.init()
 
#Initialisé la fenêtre
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS(frame per second)
fps = pygame.time.Clock()
 
# définir la postion du snake
snake_position = [100, 50]
 
# definir l'évolution du corps du serpent
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# position du "fruit"
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
#direction par défaut du serpent
direction = 'RIGHT'
change_to = direction
 
#score intiale
score = 0
 
# Afficher la fonction score
def show_score(choice, color, font, size):
   
    score_font = pygame.font.SysFont(font, size)
     
    # surface objet + score
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    #surface object
    score_rect = score_surface.get_rect()
     
    game_window.blit(score_surface, score_rect)
 
#fonction game over
def game_over():
   
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # Surface du texte + paramètre du score annoncé
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    #position du text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # quitter le programme après 5secondes lorsqu'on perd
    time.sleep(5)
     
    # désactiver pygame 
    pygame.quit()
     
    #quitter le programme
    quit()
 
 
# Main Fonction
while True:
     
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    #Choix entre 2 directions différentes jouer
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    #Bouger le serpent
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Evolution corps du serpent
    # Evolution du score avec des fruits + incrémentation de 10
    
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    #Conditions quand on perd
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    #Quandon touche le corps du serpent
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    #paramètre du score
    show_score(1, white, 'times new roman', 20)
 
    #lorsque l'on relance l'ancienne parti disparaît
    pygame.display.update()
 
    #Frame Per Second
    fps.tick(snake_speed)