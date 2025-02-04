import pygame
import constantes



pygame.init()
screen = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
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
    pygame.draw.circle(screen, "red", player_pos, constantes.JUGADOR_TAMANO)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        delta_y = (0,-1*constantes.DELTA) [player_pos.y - constantes.JUGADOR_TAMANO > 0]
     #   player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        delta_y = (0,1*constantes.DELTA) [player_pos.y - constantes.JUGADOR_TAMANO > 0]
     #   player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        delta_x=(0,1*constantes.DELTA) [player_pos.x - constantes.JUGADOR_TAMANO > 0]
     #   player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        delta_x=(0,-1*constantes.DELTA) [player_pos.x - constantes.JUGADOR_TAMANO > 0]
     #   player_pos.x += 300 * dt



    player_pos.x = max(constantes.JUGADOR_TAMANO+1, min(player_pos.x, constantes.ANCHO-constantes.JUGADOR_TAMANO))-delta_x
    player_pos.y = max(constantes.JUGADOR_TAMANO+1-delta_y, min(player_pos.y, constantes.ALTO-constantes.JUGADOR_TAMANO))+delta_y
    pygame.display.flip()
    dt = clock.tick(60)/1000
    print(dt)
pygame.quit()
