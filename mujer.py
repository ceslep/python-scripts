import pygame
import sys
from preguntas import preguntas  # Importamos la lista de preguntas desde preguntas.py

# -------------------------
#  Cargar Pygame e iniciar
# -------------------------
pygame.init()

# Tamaño de la pantalla
WIDTH, HEIGHT = 1024, 768
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia - Día Internacional de la Mujer")

# -------------------------
#  Colores
# -------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GRAY = (200, 200, 200)
HOVER_COLOR = (150, 150, 150)   # Color al pasar el mouse

# -------------------------
#  Fuentes de texto
# -------------------------
FONT = pygame.font.SysFont("Arial", 24)
FONT_TITLE = pygame.font.SysFont("Arial", 36, bold=True)
FONT_SCORE = pygame.font.SysFont("Arial", 20, bold=True)

# -------------------------
#  Cargar sonidos
# -------------------------
try:
    correct_sound = pygame.mixer.Sound("assets/correct.mp3")
    incorrect_sound = pygame.mixer.Sound("assets/incorrect.mp3")
except pygame.error:
    correct_sound = None
    incorrect_sound = None
    print("No se pudieron cargar los sonidos. Asegúrate de que los archivos existan.")

# -------------------------
#  Cargar imagen de fondo
# -------------------------
try:
    background = pygame.image.load("assets/background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error:
    background = None
    print("No se pudo cargar la imagen de fondo. Asegúrate de que el archivo exista.")

# Variables de control del juego
indice_pregunta = 0  # Índice de la pregunta actual
score_team1 = 0
score_team2 = 0
turno_equipo = 1  # Comienza el Equipo 1
game_over = False

def draw_text(text, font, color, surface, x, y):
    """Dibuja texto centrado en (x, y)."""
    render_text = font.render(text, True, color)
    rect = render_text.get_rect()
    rect.center = (x, y)
    surface.blit(render_text, rect)

def mostrar_marcador(score1, score2, turno):
    """Dibuja el marcador de puntajes y el turno actual."""
    marcador_text = f"Equipo 1: {score1}  |  Equipo 2: {score2}"
    turno_text = f"Turno de: Equipo {turno}"

    text_surface_marcador = FONT_SCORE.render(marcador_text, True, BLACK)
    SCREEN.blit(text_surface_marcador, (20, 10))

    text_surface_turno = FONT_SCORE.render(turno_text, True, BLACK)
    SCREEN.blit(text_surface_turno, (WIDTH - 180, 10))

def mostrar_pregunta(pregunta_dict, hovered_index, turno):
    """
    Muestra la pregunta y sus opciones (enumeradas) en pantalla y retorna
    la lista de rectángulos correspondientes a cada opción.
    """
    # Dibujar imagen de fondo y aclararla
    if background:
        SCREEN.blit(background, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 90))  # Ajusta el valor para aclarar la imagen
        SCREEN.blit(overlay, (0, 0))
    else:
        SCREEN.fill(WHITE)

    # Mostrar marcador
    mostrar_marcador(score_team1, score_team2, turno)

    # Título
    draw_text("Trivia - Día Internacional de la Mujer", FONT_TITLE, PURPLE, SCREEN, WIDTH // 2, 60)

    # Pregunta centrada
    draw_text(pregunta_dict["pregunta"], FONT, BLACK, SCREEN, WIDTH // 2, 180)

    # Opciones enumeradas
    LETTERS = ["a)", "b)", "c)", "d)"]
    option_rects = []
    start_y = 260
    gap = 60
    rect_width = 600
    rect_x = (WIDTH - rect_width) // 2

    for i, opcion in enumerate(pregunta_dict["opciones"]):
        color_rect = HOVER_COLOR if i == hovered_index else GRAY
        rect_y = start_y + i * gap
        rect_height = 40

        rect_opcion = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        option_rects.append(rect_opcion)

        pygame.draw.rect(SCREEN, color_rect, rect_opcion, border_radius=5)
        opcion_text = f"{LETTERS[i]} {opcion}"
        text_surface = FONT.render(opcion_text, True, BLACK)
        text_rect = text_surface.get_rect(center=rect_opcion.center)
        SCREEN.blit(text_surface, text_rect)

    return option_rects

def mostrar_resultado_final(score1, score2, total_preguntas):
    """Muestra la pantalla final con los resultados."""
    if background:
        SCREEN.blit(background, (0, 0))
    else:
        SCREEN.fill(WHITE)

    draw_text("¡Fin de la Trivia!", FONT_TITLE, PURPLE, SCREEN, WIDTH // 2, HEIGHT // 2 - 50)
    resultado_text = f"Equipo 1: {score1} puntos  |  Equipo 2: {score2} puntos"
    draw_text(resultado_text, FONT, BLACK, SCREEN, WIDTH // 2, HEIGHT // 2)
    final_msg = "Gracias por participar y conmemorar el Día Internacional de la Mujer."
    draw_text(final_msg, FONT, BLACK, SCREEN, WIDTH // 2, HEIGHT // 2 + 50)

    pygame.display.update()
    pygame.time.wait(5000)

def main():
    global indice_pregunta, score_team1, score_team2, turno_equipo, game_over

    clock = pygame.time.Clock()
    hovered_index = -1

    # Mapeo de teclas para las opciones: a->0, b->1, c->2, d->3
    key_mapping = {
        pygame.K_a: 0,
        pygame.K_b: 1,
        pygame.K_c: 2,
        pygame.K_d: 3
    }

    running = True
    while running:
        clock.tick(30)

        if not game_over:
            if indice_pregunta < len(preguntas):
                current_question = preguntas[indice_pregunta]

                option_rects = mostrar_pregunta(current_question, hovered_index, turno_equipo)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == pygame.MOUSEMOTION:
                        mouse_x, mouse_y = event.pos
                        hovered_index = -1
                        for i, rect_opcion in enumerate(option_rects):
                            if rect_opcion.collidepoint(mouse_x, mouse_y):
                                hovered_index = i
                                break

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 and hovered_index != -1:
                            # Procesar respuesta vía mouse
                            respuesta = hovered_index
                            procesar_respuesta(current_question, respuesta)
                    
                    elif event.type == pygame.KEYDOWN:
                        if event.key in key_mapping:
                            respuesta = key_mapping[event.key]
                            # Verifica que la opción existe (en caso de que la pregunta tenga menos de 4 opciones)
                            if respuesta < len(current_question["opciones"]):
                                procesar_respuesta(current_question, respuesta)

            else:
                game_over = True
                mostrar_resultado_final(score_team1, score_team2, len(preguntas))
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def procesar_respuesta(current_question, respuesta):
    """
    Procesa la respuesta (ya sea por mouse o teclado), reproduce el sonido
    correspondiente, actualiza la puntuación, cambia el turno y avanza la pregunta.
    """
    global indice_pregunta, score_team1, score_team2, turno_equipo, hovered_index

    if respuesta == current_question["respuesta_correcta"]:
        if turno_equipo == 1:
            score_team1 += 1
        else:
            score_team2 += 1

        if correct_sound:
            correct_sound.play()
            pygame.time.wait(5000)  # Espera 2 segundos
            correct_sound.stop()
    else:
        if incorrect_sound:
            incorrect_sound.play()

    print("Explicación:", current_question["explicacion"])

    # Cambiar turno automáticamente
    turno_equipo = 2 if turno_equipo == 1 else 1

    # Avanzar a la siguiente pregunta
    indice_pregunta += 1

    # Reiniciar la variable de opción seleccionada
    hovered_index = -1

if __name__ == "__main__":
    main()
