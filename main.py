from tkinter import *
from Module import *
import random as random
import numpy as np
import time
import matplotlib.pyplot as plt

root = Tk()
root.wm_title('Space')
width = 1675
height = 900
canvas = Canvas(root, width = width, height=height, bg='black')
canvas.grid(row=0, column=0)
Planetes = []
NbPlanetes = 2000
fps = 120
Circular = False
Universe = Universe(1, [width, height], 'Pool', NbPlanetes, Circular = Circular, diffusive = False)
#Universe.create_sun(1000)
Universe.create_planetes()
Planetes = Universe.Planetes

# Masse = [1.989e30, 3.285e23, 4.867e24, 5.972e24,  6.39e23]#kg
# Rayon = [20, 0.38*10, 0.9497*10, 1*10, 0.53*10]
# pos=[0, 61.741e6, 107.74e6, 147.15e6, 232.93e6]*1000 #m
# theta = [0, 317, 81, 91, 231]#deg
# vr = [0, -8.73, -0.18, -0.09, -2.18]*1000 #m/s
# def convert_distance(value):
#     return value*width/pos[-1]

T = 0
Tx = True 
while Tx == True:
    T+=1
    canvas.delete('all')

    if len(Planetes) >= 40:
        boundary = rectangle(width/2, height/2, width, height)
        qt = quadtree(boundary, 10)
        bh = Barnes_hut(Planetes, qt, canvas, Universe.Boundary, Universe.diffusive, draw_qt = False, draw_soi = False)
        sumpos = bh.sumpos
        summ = bh.summ
        method = bh.method
    else:
        Nat = Natural_method(Planetes, canvas, Universe.Boundary, Universe.diffusive)
        sumpos = Nat.sumpos
        summ = Nat.summ
        method = Nat.method

    barycentre = sumpos/summ
    canvas.create_text(barycentre[0], barycentre[1], text = "+", fill = 'white', anchor = NW)
    canvas.create_text(50, 40, text = "Time: "+str(round(T/fps,2)), fill = 'white', anchor = W)
    canvas.create_text(50, 20, text = "Nb planetes: "+str(len(Planetes)), fill = 'white', anchor = W)
    canvas.create_text(50, 60, text = method, fill = 'white', anchor = W)
    canvas.update()
    
    time.sleep(1/fps)
    if T/fps>=100 or len(Planetes)==1:
        Tx=False
root.destroy()
root.mainloop()
