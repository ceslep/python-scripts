import pygame

# `ANCHO = 800` is defining a constant variable named `ANCHO` with a value of 800. This variable is
# used to set the width of the game screen in pixels.
ANCHO = 800
ALTO = 600
JUGADOR_TAMANO = 40
DELTA=10

pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
dt = 0

movimiento_x = 0
movimiento_y = 0

delta_x=0
delta_y=0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type==pygame.KEYUP:
            delta_x=0
            delta_y=0
    screen.fill("purple")

    clock.tick(60)
    pygame.draw.circle(screen, "red", player_pos, JUGADOR_TAMANO)
    keys = pygame.key.get_pressed()

    print(delta_y)
    print(player_pos.y - JUGADOR_TAMANO > 0)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        delta_y = (0,-1*DELTA) [player_pos.y - JUGADOR_TAMANO > 0]
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        delta_y = (0,1*DELTA) [player_pos.y - JUGADOR_TAMANO > 0]
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        delta_x=(0,1*DELTA) [player_pos.x - JUGADOR_TAMANO > 0]
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        delta_x=(0,-1*DELTA) [player_pos.x - JUGADOR_TAMANO > 0]
        player_pos.x += 300 * dt



    player_pos.x = max(JUGADOR_TAMANO, min(player_pos.x, ANCHO-JUGADOR_TAMANO))-delta_x
    player_pos.y = max(JUGADOR_TAMANO-delta_y, min(player_pos.y, ALTO-JUGADOR_TAMANO))+delta_y
    pygame.display.flip()
    dt = clock.tick(60)/1000
pygame.quit()
