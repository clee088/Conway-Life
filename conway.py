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
blackline = LineStyle(1, black)
coolcolor = Color(0x00DCDF, 1)

Grid = RectangleAsset(500, 500, noline, white)
Grid = Sprite(Grid, (0,0))

run = False
#===============================================================================
class grid(Sprite):
    def __init__(self, position):
        g = RectangleAsset(50, 50, noline, white)
        super().__init__(g, position)
        
class cell(Sprite):
    def __init__(self, position):
        cc = RectangleAsset(50, 50, noline, black)
        super().__init__(cc, position)
        self.visible = False
class alivecell(Sprite):
    def __init__(self, position):
        ac = RectangleAsset(50, 50, noline, coolcolor)
        super().__init__(ac, position)
        self.visible = False
        
#===============================================================================
def row(x):
    xx = x
    y = 0
    for i in range(10):
        grid((xx, y))
        cell((xx, y))
        alivecell((xx, y))
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
        map.listenMouseEvent('click', self.mouseClick)
        #map.listenKeyEvent('keydown', 'space', self.spacePress)
#-------------------------------------------------------------------------------
    #def step(self):
        
        
#-------------------------------------------------------------------------------
            
    def mouseClick(self, event):
        x = floor(event.x / 50) * 50
        y = floor(event.y / 50) * 50
        coord = (x, y)
        if alivecell(coord).visible == False:
            alivecell(coord).visible = True
        else:
            alivecell(coord).visible = False
        
    #def spacePress(self, event):
        
#===============================================================================


myapp = map()
myapp.run()