import pygame
import sys
import random

# ============================
# FUNCIONES DE GENERACIÓN DEL LABERINTO
# ============================

def generar_laberinto(ancho, alto):
    """
    Genera un laberinto aleatorio usando backtracking recursivo.
    ancho y alto deben ser impares.
    Devuelve una matriz (lista de listas) donde '#' representa pared y ' ' pasillo.
    """
    # Inicializamos la matriz con paredes
    lab = [['#' for _ in range(ancho)] for _ in range(alto)]
    
    # Punto de inicio: (1, 1)
    inicio = (1, 1)
    lab[inicio[1]][inicio[0]] = ' '
    stack = [inicio]
    
    while stack:
        x, y = stack[-1]
        # Vecinos: desplazamientos de dos en cada dirección
        vecinos = []
        for dx, dy in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ancho and 0 <= ny < alto:
                if lab[ny][nx] == '#':
                    vecinos.append((nx, ny, dx, dy))
        if vecinos:
            nx, ny, dx, dy = random.choice(vecinos)
            # Abrir el muro intermedio
            lab[y + dy // 2][x + dx // 2] = ' '
            lab[ny][nx] = ' '
            stack.append((nx, ny))
        else:
            stack.pop()
    return lab

def laberinto_a_cadenas(lab):
    """
    Convierte la matriz del laberinto a una lista de cadenas (opcional).
    """
    return ["".join(fila) for fila in lab]

# ============================
# CONFIGURACIÓN DEL JUEGO
# ============================

# Dimensiones del laberinto (usar números impares)
COLUMNAS = 21
FILAS = 21
TAM_CELDA = 25  # Tamaño de cada celda en píxeles

# Dimensiones de la ventana
ANCHO = COLUMNAS * TAM_CELDA
ALTO = FILAS * TAM_CELDA

# Colores (RGB)
COLOR_FONDO = (0, 0, 0)
COLOR_PARED = (100, 100, 100)
COLOR_JUGADOR = (0, 0, 255)
COLOR_SALIDA = (0, 255, 0)

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto Aleatorio")

# Fuente para mensaje de victoria
fuente = pygame.font.SysFont("Arial", 40)

# ============================
# GENERAR EL LABERINTO
# ============================
laberinto = generar_laberinto(COLUMNAS, FILAS)

# Colocar posición de inicio y salida:
# - Inicio en (1,1)
# - Salida en (COLUMNAS-2, FILAS-2)
laberinto[1][1] = 'P'   # Marcamos el inicio, aunque internamente lo usaremos para mover al jugador
laberinto[FILAS-2][COLUMNAS-2] = 'S'

# Encontrar posición inicial del jugador
pos_jugador = [1, 1]  # [columna, fila]

# ============================
# BUCLE PRINCIPAL DEL JUEGO
# ============================
reloj = pygame.time.Clock()
jugando = True
ganaste = False

while jugando:
    reloj.tick(10)  # 10 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN and not ganaste:
            nueva_pos = pos_jugador.copy()
            if evento.key == pygame.K_UP:
                nueva_pos[1] -= 1
            elif evento.key == pygame.K_DOWN:
                nueva_pos[1] += 1
            elif evento.key == pygame.K_LEFT:
                nueva_pos[0] -= 1
            elif evento.key == pygame.K_RIGHT:
                nueva_pos[0] += 1

            # Verificar que la nueva posición esté dentro de los límites
            if 0 <= nueva_pos[0] < COLUMNAS and 0 <= nueva_pos[1] < FILAS:
                # Solo se mueve si la celda no es pared
                if laberinto[nueva_pos[1]][nueva_pos[0]] != '#':
                    pos_jugador = nueva_pos

    # Verificar si el jugador alcanzó la salida
    if laberinto[pos_jugador[1]][pos_jugador[0]] == 'S':
        ganaste = True

    # Dibujar fondo
    pantalla.fill(COLOR_FONDO)

    # Dibujar el laberinto
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            x = columna * TAM_CELDA
            y = fila * TAM_CELDA
            celda = laberinto[fila][columna]
            if celda == '#':
                pygame.draw.rect(pantalla, COLOR_PARED, (x, y, TAM_CELDA, TAM_CELDA))
            elif celda == 'S':
                pygame.draw.rect(pantalla, COLOR_SALIDA, (x, y, TAM_CELDA, TAM_CELDA))

    # Dibujar al jugador (si aún no ganó, se dibuja sobre la celda)
    if not ganaste:
        jugador_x = pos_jugador[0] * TAM_CELDA
        jugador_y = pos_jugador[1] * TAM_CELDA
        pygame.draw.rect(pantalla, COLOR_JUGADOR, (jugador_x, jugador_y, TAM_CELDA, TAM_CELDA))
    else:
        # Mostrar mensaje de victoria
        texto = fuente.render("¡Ganaste!", True, (255, 255, 0))
        rect_texto = texto.get_rect(center=(ANCHO//2, ALTO//2))
        pantalla.blit(texto, rect_texto)

    pygame.display.flip()

pygame.quit()
sys.exit()
