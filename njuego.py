import pygame



ANCHO=1280
ALTO=720
jugador_tamano=50



pygame.init()
screen=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()
running=True

player_pos=pygame.Vector2(ANCHO//2,ALTO//2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False
    screen.fill("purple")

    pygame.draw.circle(screen,"red",player_pos,jugador_tamano)

    if keys[pygame.K_LEFT]:
        player_pos.x-=5
    if keys[pygame.K_RIGHT]:
        player_pos.x+=5
    if keys[pygame.K_UP]:
        player_pos.y-=5
    if keys[pygame.K_DOWN]:
        player_pos.y+=5


    player_pos.x=max(jugador_tamano,min(player_pos.x,ANCHO-jugador_tamano))
    player_pos.y=max(jugador_tamano,min(player_pos.y,ALTO-jugador_tamano))    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()