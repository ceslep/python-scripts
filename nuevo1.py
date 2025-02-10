import pygame
import random
import constantes  # Importar las constantes desde el archivo constantes.py

pygame.init()
screen = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
clock = pygame.time.Clock()

# Cargar y escalar los sprites correctamente
player_sprites = []
for i in range(6):  # Suponiendo que tienes 6 imágenes
    img = pygame.image.load(
        f"assets/Walking/0_Fallen_Angels_Walking_00{i}.png").convert_alpha()
    img = pygame.transform.scale(
        img, (constantes.JUGADOR_TAMANO, constantes.JUGADOR_TAMANO))  # Escalar correctamente
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

# 📌 **Generar obstáculos asegurando que no aparezcan cerca del jugador**
jugador_radio_seguro = 150  # Distancia mínima desde el jugador
obstaculos = []

for _ in range(5):  # Número de obstáculos
    while True:
        obs_x = random.randint(50, constantes.ANCHO - 50)
        obs_y = random.randint(50, constantes.ALTO - 50)

        # Calcular distancia al jugador
        distancia = ((obs_x - player_pos.x) ** 2 + (obs_y - player_pos.y) ** 2) ** 0.5

        if distancia > jugador_radio_seguro:  # Si el obstáculo está suficientemente lejos
            if random.choice([True, False]):
                ancho = random.randint(50, 120)
                alto = random.randint(50, 120)
                obstaculos.append(("rect", pygame.Rect(obs_x, obs_y, ancho, alto)))
            else:
                radio = random.randint(30, 60)
                obstaculos.append(("circle", (obs_x, obs_y, radio)))

            break  # Salir del bucle cuando el obstáculo es válido

# Crear máscaras para colisiones con rectángulos
obstaculo_masks = [pygame.mask.Mask((obs[1].width, obs[1].height), fill=True) if obs[0] == "rect" else None for obs in obstaculos]

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
    player_mask = pygame.mask.from_surface(player_image)

    # Crear el rectángulo del jugador en la nueva posición
    player_rect = pygame.Rect(
        nueva_pos.x, nueva_pos.y, constantes.JUGADOR_TAMANO, constantes.JUGADOR_TAMANO
    )

    # **Verificar colisión con TODOS los obstáculos**
    colision = False
    for i, obs in enumerate(obstaculos):
        if obs[0] == "rect":
            offset_x = obs[1].x - player_rect.x
            offset_y = obs[1].y - player_rect.y
            if player_mask.overlap(obstaculo_masks[i], (offset_x, offset_y)):
                colision = True
                break  # Si hay colisión, detener el chequeo

        elif obs[0] == "circle":  # Verificar colisión con círculos
            dx = nueva_pos.x + constantes.JUGADOR_TAMANO // 2 - obs[1][0]
            dy = nueva_pos.y + constantes.JUGADOR_TAMANO // 2 - obs[1][1]
            distancia = (dx**2 + dy**2) ** 0.5
            if distancia < obs[1][2] + constantes.JUGADOR_TAMANO // 4:
                colision = True
                break

    if not colision:  
        player_pos = nueva_pos  # Solo actualiza la posición si NO hay colisión

    # Limitar al jugador dentro de la pantalla
    player_pos.x = max(0, min(player_pos.x, constantes.ANCHO - constantes.JUGADOR_TAMANO))
    player_pos.y = max(0, min(player_pos.y, constantes.ALTO - constantes.JUGADOR_TAMANO))

    # Control de animación
    if moving:
        frame_counter += animation_speed * dt
        if frame_counter >= 1:  # Cambiar de frame cuando el contador llegue a 1
            frame_index = (frame_index + 1) % len(player_sprites)
            frame_counter = 0  # Reiniciar el contador

    # Obtener el sprite actual
    player_image = player_sprites[frame_index]

    # Si el personaje está mirando a la izquierda, voltear la imagen
    if mirando_izquierda:
        player_image = pygame.transform.flip(player_image, True, False)

    # 🔵 Dibujar en pantalla
    screen.fill("purple")

    # 🔴 Dibujar obstáculos (rectángulos y círculos)
    for obs in obstaculos:
        if obs[0] == "rect":
            pygame.draw.rect(screen, "red", obs[1])  # Dibujar rectángulo
        elif obs[0] == "circle":
            pygame.draw.circle(screen, "blue", (obs[1][0], obs[1][1]), obs[1][2])  # Dibujar círculo

    # 🏃 Dibujar el personaje
    screen.blit(player_image, player_pos)

    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()
