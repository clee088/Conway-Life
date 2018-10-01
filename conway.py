"""
conway.py
Author: Christopher Lee
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import *

class cell(Sprite):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        white = Color(0xFFFF, 0)
        grey = Color(0xC0C0C0, 1)
        cell = RectangleAsset(100, 100, noline, white)
        

class map(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        white = Color(0xFFFF, 0)
        grey = Color(0xC0C0C0, 1)
        noline = LineStyle(1, grey)
        grid = RectangleAsset(500, 500, noline, white)
        grid = Sprite(grid, (0,0))
        cell((0,0))


myapp = map()
myapp.run()