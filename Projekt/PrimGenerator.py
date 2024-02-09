import numpy as np
import random
import time
import pygame
import tkinter as tk
from tkinter import messagebox

CELL_SIZE = 20
TIME = 0.02

UP, RIGHT, DOWN, LEFT = 1, 2, 4, 8
VISITED = 16
TO_VISIT = 32
OPPOSITE = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}

class Maze:
    "Podstawowa klasa labiryntu"

    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def create_grid(self):
        "Tworzenie obszaru labiryntu"

        return np.zeros((self.WIDTH, self.HEIGHT), dtype=int)

class Prim:
    "Klasa algorytmu Prima"

    def __init__(self, maze):
        self.maze = maze
        self.visited = maze.create_grid()
        self.to_visit = []

    def visit(self, cell):
        "Odwiedź komórkę i dodaj komórki, które mogą zostać odwiedzone"

        self.visited[cell[0]][cell[1]] |= VISITED

        self.add_to_visit((cell[0] - 1, cell[1]))
        self.add_to_visit((cell[0] + 1, cell[1]))
        self.add_to_visit((cell[0], cell[1] - 1))
        self.add_to_visit((cell[0], cell[1] + 1))

    def add_to_visit(self, cell):
        "Dodaj komórkę do odwiedzenia"

        if 0 <= cell[0] < len(self.visited) and 0 <= cell[1] < len(self.visited[1]) and self.visited[cell[0]][cell[1]] == 0:
            self.visited[cell[0]][cell[1]] |= TO_VISIT
            self.to_visit.append(cell)

    def get_neighbours(self, cell):
        "Pozyskiwanie sąsiadów komórki"

        neighbours = []

        # Górny sąsiad
        if cell[1] > 0 and self.visited[cell[0]][cell[1] - 1] & VISITED != 0:
            neighbours.append((cell[0], cell[1] - 1))

        # Lewy sąsiad
        if cell[0] > 0 and self.visited[cell[0] - 1][cell[1]] & VISITED != 0:
            neighbours.append((cell[0] - 1, cell[1]))

        # Prawy sąsiad
        if cell[0] < self.maze.WIDTH - 1 and self.visited[cell[0] + 1][cell[1]] & VISITED != 0:
            neighbours.append((cell[0] + 1, cell[1]))

        # Dolny sąsiad
        if cell[1] < self.maze.HEIGHT - 1 and self.visited[cell[0]][cell[1] + 1] & VISITED != 0:
            neighbours.append((cell[0], cell[1] + 1))

        return neighbours

    def prim_algorithm(self, drawing_func):
        "Tworzenie labiryntu za pomocą algorytmu Prima"

        def get_direction(x1, y1, x2, y2):
            "Ustalenie kierunku poruszania"

            if y1 > y2:
                return UP
            elif x1 > x2:
                return LEFT
            elif x1 < x2:
                return RIGHT
            elif y1 < y2:
                return DOWN

        self.visit((random.randint(0, self.maze.WIDTH - 1), random.randint(0, self.maze.HEIGHT - 1)))

        drawing_func(self.visited)

        while self.to_visit:
            x, y = self.to_visit.pop(random.randint(0, len(self.to_visit) - 1))
            neighbour = self.get_neighbours((x, y))
            nx, ny = neighbour[random.randint(0, len(neighbour) - 1)]

            direction = get_direction(x, y, nx, ny)
            self.visited[x][y] |= direction
            self.visited[nx][ny] |= OPPOSITE[direction]

            self.visit((x, y))

            drawing_func(self.visited)
            time.sleep(TIME)

def draw_maze(grid):
    screen.fill(WHITE)

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            x_pos = x * CELL_SIZE + padding
            y_pos = y * CELL_SIZE + padding

            if cell & UP == 0:
                pygame.draw.line(screen, BLACK, (x_pos, y_pos), ((x + 1) * CELL_SIZE + padding, y_pos))
            if cell & DOWN == 0:
                pygame.draw.line(screen, BLACK, (x_pos, (y + 1) * CELL_SIZE + padding), ((x + 1) * CELL_SIZE + padding, (y + 1) * CELL_SIZE + padding))
            if cell & LEFT == 0:
                pygame.draw.line(screen, BLACK, (x_pos, y_pos), (x_pos, (y + 1) * CELL_SIZE + padding))
            if cell & RIGHT == 0:
                pygame.draw.line(screen, BLACK, ((x + 1) * CELL_SIZE + padding, y_pos), ((x + 1) * CELL_SIZE + padding, (y + 1) * CELL_SIZE + padding))

    pygame.display.flip()

class Menu:
    "Klasa menu startowego"

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu")

        self.label_height = tk.Label(self.root, text="Podaj wysokość labiryntu:", font=("Arial", 14))
        self.label_height.pack(pady = (50, 10))
        self.entry_height = tk.Entry(self.root, font=("Arial", 14), justify='center')
        self.entry_height.insert(0, "10") 
        self.entry_height.pack()

        self.label_width = tk.Label(self.root, text="Podaj szerokość labiryntu:", font=("Arial", 14))
        self.label_width.pack(pady = (10, 10))
        self.entry_width = tk.Entry(self.root, font=("Arial", 14), justify='center')
        self.entry_width.insert(0, "10") 
        self.entry_width.pack()

        self.button_start = tk.Button(self.root, text="START", command=self.check, font=("Arial", 14))
        self.button_start.pack(pady = (10, 0))

        width = 300
        height = 300
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.mainloop()

    def check(self):
        "Funkcja sprawdzająca input od użytkownika"

        height = self.entry_height.get()
        width = self.entry_width.get()
        try:
            height = int(height)
            width = int(width)
            if height <= 1 or width <= 1:
                raise ValueError
            self.root.destroy()
            self.run(height, width)
        except ValueError:
            messagebox.showerror("Błąd", "Wysokość i szerokość muszą być dodatnimi liczbami całkowitymi większymi od 1")

    def run(self, height, width):
        "Funkcja wyświetlająca labirynt za pomocą modułu pygame"

        pygame.init()

        global padding, screen_WIDTH, screen_HEIGHT, screen, BLACK, WHITE

        padding = 40
        screen_WIDTH = width * CELL_SIZE + 2 * padding
        screen_HEIGHT = height * CELL_SIZE + 2 * padding
        screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
        pygame.display.set_caption('')

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        maze = Maze(width, height)
        prim = Prim(maze)

        prim.prim_algorithm(draw_maze)

        pygame.image.save(screen, "maze.png")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

def main():
    start_menu = Menu()
    start_menu.root.mainloop()

if __name__ == "__main__":
    main()
