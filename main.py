from tkinter import *
from constants import *
import random
def draw_grid():
    for row in range(height_screen):  # Loop through the rows
        for col in range(width_screen):  # Loop through the columns
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 +cell_size
                # If the cell is alive
                if grid[row][col] == 1:
                   canvas.create_rectangle(
                        x1, y1, x2, y2, fill='blue', outline='black')
                # If the cell is dead
                else:
                    canvas.create_rectangle(
                        x1, y1, x2, y2, fill='white', outline='black')
def create_grid():
      grid = []
      for row in range(height_screen):  # Loop through the rows
            grid.append([])
            for col in range(width_screen):  # Loop through the columns
                # Append a random number to the grid
                grid[row].append(random.randint(0, 1))
      return grid
root = Tk()
root.title("Game of life")
config_screen= "{0}x{1}".format(width_screen,height_screen)
root.geometry(config_screen)
root.minsize(min_width_screen,min_height_screen)
grid = create_grid()
canvas = Canvas(root,width=width_screen*cell_size,height=height_screen*cell_size,bg="white")
canvas.pack()
draw_grid()

root.mainloop() 

