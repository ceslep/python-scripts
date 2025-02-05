import pygame
import constantes

pygame.init()
screen = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
clock = pygame.time.Clock()

# Cargar los sprites de animación en una lista
player_sprites = [
    pygame.image.load(f"assets/Walking/0_Fallen_Angels_Walking_00{i}.png").convert_alpha()
    for i in range(6)  # Ajusta el número de imágenes
]

# Escalar las imágenes (opcional)
player_sprites = [pygame.transform.scale(img, (constantes.JUGADOR_TAMANO, constantes.JUGADOR_TAMANO)) for img in player_sprites]

# Variables del jugador
player_pos = pygame.Vector2(constantes.ANCHO // 2-constantes.JUGADOR_TAMANO//2, constantes.ALTO // 2-constantes.JUGADOR_TAMANO//2)
print(player_pos)

velocidad = constantes.VELOCIDAD  
frame_index = 0  # Índice del sprite actual
animation_speed = constantes.JUGADOR_SPEED  # Velocidad de cambio de animación
frame_counter = 0  # Contador para el cambio de animación
mirando_izquierda = False  # Dirección inicial

running = True
while running:
    dt = clock.tick(60) / 1000.0  # Control de FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Lógica de movimiento
    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Izquierda
        player_pos.x -= velocidad * dt
        mirando_izquierda = True
        moving = True

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Derecha
        player_pos.x += velocidad * dt
        mirando_izquierda = False
        moving = True

    if keys[pygame.K_w] or keys[pygame.K_UP]:  # Arriba
        player_pos.y -= velocidad * dt
        moving = True

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Abajo
        player_pos.y += velocidad * dt
        moving = True

    # Obtener el sprite actual
    player_image = player_sprites[frame_index]

    # Limitar la posición del jugador dentro de la pantalla
    player_pos.x = max(0, min(player_pos.x, constantes.ANCHO - player_image.get_width()))
    player_pos.y = max(0, min(player_pos.y, constantes.ALTO - player_image.get_height()))

    # Obtener el rectángulo del personaje en la posición correcta
    player_rect = player_image.get_rect(topleft=(player_pos.x, player_pos.y))

    # Si el personaje está mirando a la izquierda, voltear la imagen
    if mirando_izquierda:
        player_image = pygame.transform.flip(player_image, True, False)

    # Dibujar en pantalla
    screen.fill("purple")  
    pygame.draw.rect(screen, "yellow", player_rect, 2)  # Rectángulo amarillo alrededor del jugador
    screen.blit(player_image, player_pos)  # Dibujar el personaje

    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()
