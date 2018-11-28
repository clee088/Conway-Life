"""
conway.py
Author: Christopher Lee
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
#==================================IMPORTS======================================
from ggame import *
from math import floor
#==============================COLORS_AND_LINES=================================
black = Color(0, 1)
white = Color(0xffffff, 1)
pink = Color(0xFF0097, 1)
blue = Color(0x00B6FF, 1)
line = LineStyle(1, white)
blackline = LineStyle(0.1, black)
c = {}
#================================IMPORTANT======================================
'''gridnumber is the number of cells that there are for each row
Recommended is 20. Max is 30 before program starts to slow'''
#gridnumber = 20
gridnumber = int(input('''How many cells would you like each row to have?
Recommended is 20 cells.
Max is 30 cells before program starts to slow.
'''))
#Scales screen based on gridnumber
ScreenWidth = gridnumber * 100
ScreenHeight = gridnumber * 100
#=================================CLASSES=======================================
class grid(Sprite):
    g = RectangleAsset(50, 50, blackline, white)
    def __init__(self, position):
        super().__init__(grid.g, position)
        self.visible = True
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
#================================CREATES GRID===================================
def row(x):
    xx = x
    y = 0
    for i in range(gridnumber):
        grid((xx, y))
        cell((xx, y))
        deadcell((xx, y))
        y += 50
#----------------------------------RULES----------------------------------------
def rules():
    print('''RULES: 
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.

2. Any live cell with two or three live neighbors lives on to the next generation.

3. Any live cell with more than three live neighbors dies, as if by overpopulation.

4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

HOW TO PLAY:
- Click where you want to add a cell to the grid
- Press R to move to the next generation
- Press C to reset / clear the grid''')
#==============================RUNNING_PROGRAM==================================
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
        map.listenKeyEvent('keydown', 'c', self.c)
#----------------------------------STEP_FUNC------------------------------------
    def step(self):
        if self.go == True:
            coordlist = []
            for (xc, yc) in c:
                coordlist.append((xc, yc))
            check = []
            for (xc, yc) in coordlist:
                for x in range(xc - 50, xc + 100, 50):
                    if x <= ScreenWidth and x >= 0:
                        for y in range(yc - 50, yc + 100, 50):
                            if y <= ScreenHeight and y >= 0 and (x, y) not in check:
                                check.append((x, y))
            for (xc, yc) in check:
                exist = 0
                neighbor = []
                for x in range(xc - 50, xc + 100, 50):
                    if x <= ScreenWidth and x >= 0:
                        for y in range(yc - 50, yc + 100, 50):
                            if y <= ScreenHeight and y >= 0:
                                neighbor.append((x, y))
                #removes coord so it's not counting itself
                neighbor.remove((xc, yc))
                for (xcoord, ycoord) in neighbor:
                    if (xcoord, ycoord) in coordlist:
                        exist += 1
                if exist == 3 and (xc, yc) not in coordlist:
                    c[(xc, yc)] = 'da'
                    cell((xc, yc)).visible = True
                elif (xc, yc) in coordlist:
                    if exist == 2 or exist == 3:
                        c[(xc, yc)] = 'a'
                        cell((xc, yc)).visible = True
                    else:
                        c[(xc, yc)] = 'd'
                        grid((xc, yc)).visible = True
            '''
            for coord in c:
                if c[(x, y)] == 'a':
                    cell(coord).visible = True
                elif c[(x, y)] == 'd':
                    grid(coord).visible = True
                elif c[(x, y)] == 'da':
                    c[(x, y)] = 'a'
                    cell(coord).visible = True
            '''
            self.go = False
            print('Stopping...')
#-------------------------------MOUSE_CLICK-------------------------------------
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
#-----------------------------MOVE_TO_NEXT_GEN----------------------------------
    def r(self, event):
        self.go = not self.go
        if self.go == True:
            print('Running...')
        else:
            self.go = False
            print('Stopping...')
#----------------------------------CLEAR----------------------------------------
    def c(self, event):
        print('Clearing...')
        x = 0
        for i in range(gridnumber):
            row(x)
            x += 50
        c.clear()
#====================================RUN=======================================
myapp = map(ScreenWidth, ScreenHeight)
myapp.run()