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
frameWidth = 1600
frameHeight = 1600
#===============================================================================
#Colors and Lines
black = Color(0, 1)
white = Color(0xffffff, 1)
grey = Color(0x2E2E2E, 1)
lightgrey = Color(0x767676, 1)
red = Color(0xFF0000, 1)
green = Color(0x20CF00, 1)
lightgreen = Color(0x27FF00, 1)
coolcolor = Color(0x00DCDF, 1)
noline = LineStyle(1, grey)
blackline = LineStyle(1, black)
greenline = LineStyle(1, lightgreen)
c = {}
ac = {}
gridnumber = int(input('How many grid cells? '))
#===============================================================================
class grid(Sprite):
    def __init__(self, position):
        g = RectangleAsset(50, 50, noline, black)
        super().__init__(g, position)
class cell(Sprite):
    def __init__(self, position):
        cc = RectangleAsset(50, 50, greenline, green)
        super().__init__(cc, position)
        self.visible = False
class deadcell(Sprite):
    def __init__(self, position):
        ac = RectangleAsset(50, 50, noline, lightgrey)
        super().__init__(ac, position)
        self.visible = False
#===============================================================================
def row(x):
    xx = x
    y = 0
    for i in range(gridnumber):
        grid((xx, y))
        cell((xx, y))
        deadcell((xx, y))
        y += 50
#===============================================================================
class map(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.go = False
        print('''RULES: 
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.

2. Any live cell with two or three live neighbors lives on to the next generation.

3. Any live cell with more than three live neighbors dies, as if by overpopulation.

4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.''')
        x = 0
        for i in range(gridnumber):
            row(x)
            x += 50
        map.listenKeyEvent('keydown', 'r', self.r)
        map.listenMouseEvent('click', self.mouse)
#-------------------------------------------------------------------------------
    def step(self):
        if self.go == True:
            for coord in c:
                if c[coord] == 'a':
                    c[coord] = 'd'
                    deadcell(coord).visible = True
                    cell(coord).visible = False
            self.go = False
            print('Stopping...')
#-------------------------------------------------------------------------------
    def mouse(self, event):
        if self.go == False:
            x = floor(event.x / 50) * 50
            y = floor(event.y / 50) * 50
            coord = (x, y)
            if x >= 0 and y >= 0 and x < gridnumber * 50 and y < gridnumber * 50:
                c[coord] = 'p'
                if c[coord] == 'a':
                    c[coord] = 'd'
                    cell(coord).visible = False
                else:
                    c[coord] = 'a'
                    cell(coord).visible = True
#-------------------------------------------------------------------------------
    def r(self, event):
        self.go = not self.go
        if self.go == True:
            print('Running...')
        elif self.go == False:
            print('Stopping...')
#===============================================================================
myapp = map(frameWidth, frameHeight)
myapp.run()