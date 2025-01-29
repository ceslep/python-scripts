import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Evita los Obstáculos")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Bucle principal del juego
reloj = pygame.time.Clock()

# Variables del jugador
jugador_tamano = 50
jugador_x = ANCHO // 2 - jugador_tamano // 2
jugador_y = ALTO - jugador_tamano - 10
velocidad_jugador = 5

# Lista de obstáculos
obstaculos = []
velocidad_obstaculo = 5
frecuencia_obstaculos = 30  # Controla la frecuencia de aparición

# Puntuación
puntuacion = 0
fuente = pygame.font.SysFont(None, 36)

# Bucle principal
corriendo = True
contador_frames = 0

while corriendo:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener todas las teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jugador_x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jugador_x += velocidad_jugador
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        jugador_y -= velocidad_jugador
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        jugador_y += velocidad_jugador

    # Limitar al jugador dentro de la ventana
    jugador_x = max(0, min(jugador_x, ANCHO - jugador_tamano))
    jugador_y = max(0, min(jugador_y, ALTO - jugador_tamano))

    # Añadir nuevos obstáculos
    if contador_frames % frecuencia_obstaculos == 0:
        obstaculo_x = random.randint(0, ANCHO - jugador_tamano)
        obstaculo_y = -jugador_tamano
        obstaculos.append([obstaculo_x, obstaculo_y])

    contador_frames += 1

    # Mover obstáculos
    for obstaculo in obstaculos:
        obstaculo[1] += velocidad_obstaculo

    # Eliminar obstáculos que salieron de la pantalla
    obstaculos = [obs for obs in obstaculos if obs[1] < ALTO]

    # Detectar colisiones
    jugador_rect = pygame.Rect(jugador_x, jugador_y, jugador_tamano, jugador_tamano)
    for obs in obstaculos:
        obstaculo_rect = pygame.Rect(obs[0], obs[1], jugador_tamano, jugador_tamano)
        if jugador_rect.colliderect(obstaculo_rect):
            corriendo = False  # Fin del juego

    # Actualizar puntuación
    puntuacion += 1

    # Dibujar todo
    ventana.fill(BLANCO)  # Limpiar pantalla

    # Dibujar jugador
    pygame.draw.rect(ventana, AZUL, jugador_rect)

    # Dibujar obstáculos
    for obs in obstaculos:
        pygame.draw.rect(ventana, ROJO, (obs[0], obs[1], jugador_tamano, jugador_tamano))

    # Dibujar puntuación
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, NEGRO)
    ventana.blit(texto_puntuacion, (10, 10))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar FPS
    reloj.tick(60)

# Mostrar mensaje de fin de juego
ventana.fill(BLANCO)
texto_fin = fuente.render("¡Juego Terminado!", True, NEGRO)
texto_puntuacion_final = fuente.render(f"Puntuación Final: {puntuacion}", True, NEGRO)
ventana.blit(texto_fin, (ANCHO // 2 - texto_fin.get_width() // 2, ALTO // 2 - 50))
ventana.blit(texto_puntuacion_final, (ANCHO // 2 - texto_puntuacion_final.get_width() // 2, ALTO // 2))
pygame.display.flip()

# Esperar unos segundos antes de cerrar
pygame.time.wait(3000)

# Finalizar Pygame
pygame.quit()
sys.exit()
