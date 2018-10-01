"""
conway.py
Author: Christopher Lee
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import *
#Colors and Lines
black = Color(0, 0)
white = Color(0xffffff, 1)
grey = Color(0xC0C0C0, 1)
noline = LineStyle(1, grey)


#--
class cell(Sprite):
    def __init__(self, position):
        cell = RectangleAsset(50, 50, noline, white)
        cell = Sprite(cell)

class map(App):
    def __init__(self):
        super().__init__()
        grid = RectangleAsset(500, 500, noline, black)
        grid = Sprite(grid, (0,0))
        cell((0, 0))
        


myapp = map()
myapp.run()