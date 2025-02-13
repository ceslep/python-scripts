import pygame
import sys
import random

# Configuración inicial
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
MAZE_ROWS = SCREEN_HEIGHT // CELL_SIZE
MAZE_COLS = SCREEN_WIDTH // CELL_SIZE

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Inicializar pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Laberinto de 10 Niveles")
clock = pygame.time.Clock()

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.generate()
        
    def generate(self):
        stack = []
        current = self.grid[0][0]
        current.visited = True
        stack.append(current)
        
        while stack:
            current = stack[-1]
            neighbors = self.get_unvisited_neighbors(current)
            
            if neighbors:
                next_cell = random.choice(neighbors)
                self.remove_walls(current, next_cell)
                next_cell.visited = True
                stack.append(next_cell)
            else:
                stack.pop()
                
    def get_unvisited_neighbors(self, cell):
        neighbors = []
        row, col = cell.row, cell.col
        
        if row > 0 and not self.grid[row-1][col].visited: # Arriba
            neighbors.append(self.grid[row-1][col])
        if col < self.cols-1 and not self.grid[row][col+1].visited: # Derecha
            neighbors.append(self.grid[row][col+1])
        if row < self.rows-1 and not self.grid[row+1][col].visited: # Abajo
            neighbors.append(self.grid[row+1][col])
        if col > 0 and not self.grid[row][col-1].visited: # Izquierda
            neighbors.append(self.grid[row][col-1])
            
        return neighbors
    
    def remove_walls(self, current, next_cell):
        dr = next_cell.row - current.row
        dc = next_cell.col - current.col
        
        if dr == -1: # Arriba
            current.walls['top'] = False
            next_cell.walls['bottom'] = False
        elif dr == 1: # Abajo
            current.walls['bottom'] = False
            next_cell.walls['top'] = False
        elif dc == 1: # Derecha
            current.walls['right'] = False
            next_cell.walls['left'] = False
        elif dc == -1: # Izquierda
            current.walls['left'] = False
            next_cell.walls['right'] = False
    
    def draw(self, surface):
        for row in self.grid:
            for cell in row:
                x = cell.col * CELL_SIZE
                y = cell.row * CELL_SIZE
                
                if cell.walls['top']:
                    pygame.draw.line(surface, WHITE, (x, y), (x + CELL_SIZE, y), 2)
                if cell.walls['right']:
                    pygame.draw.line(surface, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
                if cell.walls['bottom']:
                    pygame.draw.line(surface, WHITE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
                if cell.walls['left']:
                    pygame.draw.line(surface, WHITE, (x, y), (x, y + CELL_SIZE), 2)

class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.size = CELL_SIZE // 2
        self.x = col * CELL_SIZE + (CELL_SIZE - self.size) // 2
        self.y = row * CELL_SIZE + (CELL_SIZE - self.size) // 2
        
    def move(self, direction, maze):
        current_cell = maze.grid[self.row][self.col]
        new_row, new_col = self.row, self.col
        
        if direction == 'up' and not current_cell.walls['top']:
            new_row -= 1
        elif direction == 'down' and not current_cell.walls['bottom']:
            new_row += 1
        elif direction == 'left' and not current_cell.walls['left']:
            new_col -= 1
        elif direction == 'right' and not current_cell.walls['right']:
            new_col += 1
        else:
            return False
        
        if 0 <= new_row < maze.rows and 0 <= new_col < maze.cols:
            self.row = new_row
            self.col = new_col
            self.x = new_col * CELL_SIZE + (CELL_SIZE - self.size) // 2
            self.y = new_row * CELL_SIZE + (CELL_SIZE - self.size) // 2
            return True
        return False
    
    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.size, self.size))

def draw_exit(surface, row, col):
    x = col * CELL_SIZE + (CELL_SIZE - 20) // 2
    y = row * CELL_SIZE + (CELL_SIZE - 20) // 2
    pygame.draw.rect(surface, GREEN, (x, y, 20, 20))

def game():
    current_level = 1
    total_score = 0
    max_levels = 10
    
    while current_level <= max_levels:
        maze = Maze(MAZE_ROWS, MAZE_COLS)
        player = Player(0, 0)
        exit_row = MAZE_ROWS - 1
        exit_col = MAZE_COLS - 1
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.move('up', maze)
                    if event.key == pygame.K_DOWN:
                        player.move('down', maze)
                    if event.key == pygame.K_LEFT:
                        player.move('left', maze)
                    if event.key == pygame.K_RIGHT:
                        player.move('right', maze)
            
            # Verificar si llegó a la salida
            if player.row == exit_row and player.col == exit_col:
                total_score += 100
                current_level += 1
                break
            
            # Dibujar
            screen.fill(BLACK)
            maze.draw(screen)
            player.draw(screen)
            draw_exit(screen, exit_row, exit_col)
            
            # Mostrar información
            font = pygame.font.Font(None, 36)
            text = font.render(f"Nivel: {current_level}  Puntaje: {total_score}", True, WHITE)
            screen.blit(text, (10, 10))
            
            pygame.display.flip()
            clock.tick(30)
    
    # Pantalla final
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render(f"¡GANASTE! Puntaje: {total_score}", True, GREEN)
    screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(5000)

if __name__ == "__main__":
    game()
    pygame.quit()
    sys.exit()