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
from math import floor

#===============================================================================
#Colors and Lines
black = Color(0, 1)
white = Color(0xffffff, 1)
grey = Color(0xC0C0C0, 1)
noline = LineStyle(1, grey)

Grid = RectangleAsset(500, 500, noline, white)
Grid = Sprite(Grid, (0,0))


#===============================================================================
class grid(Sprite):
    def __init__(self, position):
        g = RectangleAsset(50, 50, noline, white)
        super().__init__(g, position)
        
class cell(Sprite):
    def __init__(self, position):
        cc = RectangleAsset(50, 50, noline, black)
        super().__init__(cc, position)
        
#===============================================================================
def row(x):
    xx = x
    y = 0
    for i in range(10):
            grid((xx, y))
            y += 50
#===============================================================================
class map(App):
    def __init__(self):
        super().__init__()
        quantity = {}
        grid = RectangleAsset(500, 500, noline, white)
        grid = Sprite(grid, (0,0))
        x = 0
        for i in range(10):
            row(x)
            x += 50
        map.listenMouseEvent('click', self.mouseClick)
#-------------------------------------------------------------------------------
    def mouseClick(self, event):
        quantity = {}
        x = floor(event.x / 50) * 50
        y = floor(event.y / 50) * 50
        if x < 500 and y < 500:
            cell((x, y))
            quantity = {x, y}
            print(quantity)
        
#-------------------------------------------------------------------------------
#===============================================================================


myapp = map()
myapp.run()