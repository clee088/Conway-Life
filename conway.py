"""
conway.py
Author: Christopher Lee
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
#===============================================================================
from ggame import *
#===============================================================================
#Colors and Lines
black = Color(0, 1)
white = Color(0xffffff, 1)
grey = Color(0xC0C0C0, 1)
noline = LineStyle(1, grey)

grid = RectangleAsset(500, 500, noline, white)
grid = Sprite(grid, (0,0))
#===============================================================================
class cell(Sprite):
    def __init__(self, position):
        c = RectangleAsset(50, 50, noline, white)
        super().__init__(c, position)
        


#===============================================================================
def row(x):
    xx = x
    y = 0
    for i in range(10):
            cell((xx, y))
            y += 50
#===============================================================================
class map(App):
    def __init__(self):
        super().__init__()
        grid = RectangleAsset(500, 500, noline, white)
        grid = Sprite(grid, (0,0))
        x = 0
        for i in range(10):
            row(x)
            x += 50
            
#===============================================================================
        
myapp = map()
myapp.run()