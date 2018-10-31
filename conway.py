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
red = Color(0xFF0000, 1)

Grid = RectangleAsset(500, 500, noline, white)
Grid = Sprite(Grid, (0,0))

alive = ()
dead = ()
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
        ac = RectangleAsset(50, 50, noline, black)
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
        self.go = False
        grid = RectangleAsset(500, 500, noline, white)
        grid = Sprite(grid, (0,0))
        x = 0
        for i in range(10):
            row(x)
            x += 50
        map.listenKeyEvent('keydown', 'space', self.space)
        map.listenMouseEvent('click', self.mouse)
        
#-------------------------------------------------------------------------------
    def step(self):
        if self.go == True:
            print('hi')
        
#-------------------------------------------------------------------------------
            
    def mouse(self, event):
        if self.go == False:
            x = floor(event.x / 50) * 50
            y = floor(event.y / 50) * 50
            coord = (x, y)
            if x >= 0 and y >= 0 and x < 500 and y < 500:
                if cell(coord).visible == False:
                    cell(coord).visible = True
        
    def space(self, event):
        self.go = not self.go
        if self.go == True:
           print('Running...')
        elif self.go == False:
            print('Stopping...')
#===============================================================================


myapp = map()
myapp.run()