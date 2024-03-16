from tkinter import *
from constants import *
root = Tk()
root.title("Game of life")
config_screen= "{0}x{1}".format(width_screen,height_screen)
root.geometry(config_screen)
root.minsize(min_width_screen,min_height_screen)
mainFrame = Frame(root,width=width_screen,height=height_screen)
mainFrame.grid()

root.mainloop() #отображение окна
