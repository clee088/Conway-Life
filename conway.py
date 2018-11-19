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
pink = Color(0xFF0097, 1)
blue = Color(0x00B6FF, 1)
line = LineStyle(1, white)
blackline = LineStyle(0.1, black)
c = {}
dc = {}
ac = {}
#================================IMPORTANT======================================
'''gridnumber is the number of cells that there are for each row
Recommended is 20. Max is 30 before program starts to slow'''
gridnumber = 20
ScreenWidth = gridnumber * 100
ScreenHeight = gridnumber * 100
#===============================================================================
class grid(Sprite):
    g = RectangleAsset(50, 50, blackline, white)
    def __init__(self, position):
        super().__init__(grid.g, position)
class cell(Sprite):
    cc = RectangleAsset(50, 50, blackline, blue)
    def __init__(self, position):
        super().__init__(cell.cc, position)
        self.visible = False
class deadcell(Sprite):
    dc = RectangleAsset(50, 50, blackline, pink)
    def __init__(self, position):
        super().__init__(deadcell.dc, position)
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
#-------------------------------------------------------------------------------
def rules():
    print('''RULES: 
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.

2. Any live cell with two or three live neighbors lives on to the next generation.

3. Any live cell with more than three live neighbors dies, as if by overpopulation.

4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.''')
#===============================================================================
class map(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.go = False
        rules()
        x = 0
        for i in range(gridnumber):
            row(x)
            x += 50
        map.listenKeyEvent('keydown', 'r', self.r)
        map.listenMouseEvent('click', self.mouse)
#-------------------------------------------------------------------------------
    def step(self):
        if self.go == True:
            coordlist = []
            for (x, y) in c:
                coordlist.append((x, y))
            neighbor = []
            print(x, y)
            for (x, y) in coordlist:
                exist = 0
                for x in range(x - 1, x + 2):
                    if x <= ScreenWidth and x >= 0:
                        for y in range(y - 1, y + 2):
                            if y <= ScreenHeight and y >= 0:
                                neighbor.append((x, y))
                for (x, y) in neighbor:
                    if (x, y) in coordlist:
                        exist += 1
            
                if exist == 4:
                    #(x, y) = coord
                    c[(x, y)] = 'da'
                elif exist == 3 or x == 4:
                    #(x, y) = coord
                    c[(x, y)] = 'a'
                else:
                    #(x, y) = coord
                    c[(x, y)] = 'd'
            print(c)
            for coord in c:
                if c[(x, y)] == 'a':
                    cell(coord).visible = True
                elif c[(x, y)] == 'd':
                    deadcell(coord).visible = True
                elif c[(x, y)] == 'da':
                    cell(coord).visible = True

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
                    print('test')
                    c[coord] = 'd'
                    grid(coord).visible = True
                    
                else:
                    c[coord] = 'a'
                    cell(coord).visible = True
#-------------------------------------------------------------------------------
    def r(self, event):
        self.go = not self.go
        if self.go == True:
            print('Running...')
        else:
            self.go = False
            print('Stopping...')
#===============================================================================
myapp = map(ScreenWidth, ScreenHeight)
myapp.run()