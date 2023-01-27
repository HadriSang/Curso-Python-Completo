import pygame
import random

# Inicializar pygame
pygame.init()

# Establecer tamaño de pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Establecer título de pantalla
pygame.display.set_caption("Juego de la Culebrita")

# Establecer color de fondo
background_color = (5, 5, 5)

# Establecer tamaño de culebrita
snake_block = 10
snake_speed = 30

# Establecer posición inicial de culebrita
snake_x = 300
snake_y = 300

# Establecer dirección inicial de culebrita
snake_direction = "right"

# Establecer tamaño de comida
foodx = 0
foody = 0

# Establecer puntos
score = 0

# Establecer fuente
font_style = pygame.font.SysFont(None, 50)

# Función para mostrar puntos
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/2, screen_height/2])

# Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Movimiento de culebrita con teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = "left"
            if event.key == pygame.K_RIGHT:
                snake_direction = "right"
            if event.key == pygame.K_UP:
                snake_direction = "up"
            if event.key == pygame.K_DOWN:
                snake_direction = "down"

    # Establecer color de fondo
    screen.fill(background_color)

    # Lógica de movimiento de culebrita
    if snake_direction == "right":
        snake_x += snake_block
    if snake_direction == "left":
        snake_x -= snake_block
    if snake_direction == "up":
        snake_y -= snake_block
    if snake_direction == "down":
        snake
