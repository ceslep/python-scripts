import pygame
import constantes  # Asegúrate de que contiene ANCHO, ALTO, JUGADOR_TAMANO, VELOCIDAD, JUGADOR_SPEED

pygame.init()
screen = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
clock = pygame.time.Clock()

# Cargar y escalar los sprites correctamente
player_sprites = []
for i in range(6):  # Suponiendo que tienes 6 imágenes
    img = pygame.image.load(f"assets/Walking/0_Fallen_Angels_Walking_00{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (constantes.JUGADOR_TAMANO, constantes.JUGADOR_TAMANO))  # Escalar correctamente
    player_sprites.append(img)  # Guardar imagen escalada en la lista

# 🎯 **Centrar el jugador en la pantalla**
player_pos = pygame.Vector2(
    (constantes.ANCHO - constantes.JUGADOR_TAMANO) // 2, 
    (constantes.ALTO - constantes.JUGADOR_TAMANO) // 2
)

velocidad = constantes.VELOCIDAD  
frame_index = 0  
animation_speed = constantes.JUGADOR_SPEED  
frame_counter = 0  
mirando_izquierda = False  

# Definir una pared como un rectángulo
pared_rect = pygame.Rect(0, 200, 100, 100)

# Crear una máscara para la pared (suponiendo que es un rectángulo lleno)
pared_surf = pygame.Surface((100, 100))  
pared_surf.fill("red")  # La superficie de la pared es roja
pared_mask = pygame.mask.from_surface(pared_surf)  # Crear la máscara de colisión

running = True
while running:
    dt = clock.tick(60) / 1000.0  # Control de FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Lógica de movimiento
    keys = pygame.key.get_pressed()
    moving = False
    nueva_pos = player_pos.copy()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  
        nueva_pos.x -= velocidad * dt
        mirando_izquierda = True
        moving = True

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  
        nueva_pos.x += velocidad * dt
        mirando_izquierda = False
        moving = True

    if keys[pygame.K_w] or keys[pygame.K_UP]:  
        nueva_pos.y -= velocidad * dt
        moving = True

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:  
        nueva_pos.y += velocidad * dt
        moving = True

    # Obtener el sprite actual
    player_image = player_sprites[frame_index]

    # Obtener la máscara del jugador a partir de su imagen
    player_mask = pygame.mask.from_surface(player_image)

    # Crear el rectángulo del jugador en la nueva posición
    player_rect = pygame.Rect(nueva_pos.x, nueva_pos.y, constantes.JUGADOR_TAMANO, constantes.JUGADOR_TAMANO)

    # **Verificar colisión precisa con la máscara**
    offset_x = pared_rect.x - player_rect.x
    offset_y = pared_rect.y - player_rect.y
    if player_mask.overlap(pared_mask, (offset_x, offset_y)) is None:  
        player_pos = nueva_pos  # Solo actualiza la posición si NO hay colisión

    # Limitar al jugador dentro de la pantalla
    player_pos.x = max(0, min(player_pos.x, constantes.ANCHO - constantes.JUGADOR_TAMANO))
    player_pos.y = max(0, min(player_pos.y, constantes.ALTO - constantes.JUGADOR_TAMANO))

    # Crear nuevamente el rectángulo del personaje en la posición corregida
    player_rect = pygame.Rect(player_pos.x, player_pos.y, constantes.JUGADOR_TAMANO, constantes.JUGADOR_TAMANO)

    # Si el personaje está mirando a la izquierda, voltear la imagen
    if mirando_izquierda:
        player_image = pygame.transform.flip(player_image, True, False)

    # Dibujar en pantalla
    screen.fill("purple")  
  #  pygame.draw.rect(screen, "yellow", player_rect, 2)  # Rectángulo amarillo alrededor del jugador
    pygame.draw.rect(screen, "red", pared_rect)  # Dibujar la pared en rojo
    screen.blit(player_image, player_pos)  # Dibujar el personaje

    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()
