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
NbPlanetes = 400
fps = 120
Circular = True
# Masse = [1.989e30, 3.285e23, 4.867e24, 5.972e24,  6.39e23]#kg
# Rayon = [20, 0.38*10, 0.9497*10, 1*10, 0.53*10]
# pos=[0, 61.741e6, 107.74e6, 147.15e6, 232.93e6]*1000 #m
# theta = [0, 317, 81, 91, 231]#deg
# vr = [0, -8.73, -0.18, -0.09, -2.18]*1000 #m/s
# def convert_distance(value):
#     return value*width/pos[-1]

Planetes.append(planete(np.array([width/2, height/2], dtype=float), np.array([0, 0], dtype=float),10, 100))
for i in range(1, NbPlanetes):
    if Circular:
        theta = random.randrange(0,360)
        rh = random.randrange(100,int(height/2)+1)
        posx = rh*np.cos(theta/360*2*np.pi)+width/2
        posy = rh*np.sin(theta/360*2*np.pi)+height/2
        inv = random.randrange(0,2)
        vx = np.sqrt(Planetes[0].G*Planetes[0].m/rh)*np.cos(theta/360*2*np.pi + np.pi/2)
        vy = np.sqrt(Planetes[0].G*Planetes[0].m/rh)*np.sin(theta/360*2*np.pi + np.pi/2)
    if not Circular:
        posx = random.randrange(0,width+1)
        posy = random.randrange(0,height+1)
        vx = random.randrange(-5,5+1)/5
        vy = random.randrange(-5,5+1)/5
    r = random.randrange(1,4+1)
    Planetes.append(planete(np.array([posx, posy], dtype=float), np.array([vx, vy], dtype=float), r))

T = 0
Tx = True
KENERGY = []
PENERGY = []
methode = ''
while Tx == True:
    T+=1
    canvas.delete('all')
    boundary = rectangle(width/2, height/2, width, height)
    qt = quadtree(boundary, 10)
    sumpos=0
    summ = 0
    if len(Planetes) >= 50:
        method = 'Barnes-hut method'
        for planete1 in Planetes:
            qt.insert(planete1)
            rect = Circle(planete1.pos[0], planete1.pos[1], planete1.m+20)
            #canvas.create_oval(rect.x-rect.w, rect.y-rect.h, rect.x+rect.w, rect.y+rect.h, outline = 'green')
            points = qt.query(rect) 
            for point in points:
                planete2 = point.userdata
                if np.linalg.norm(planete1.pos-planete2.pos):
                    planete1.Fg(planete2)
                if np.linalg.norm(planete1.pos-planete2.pos) < (planete1.r + planete2.r) and planete1 != planete2:
                    if planete1.m > planete2.m:
                        planete1.agglo(planete2)
                        try:
                            Planetes.remove(planete2)
                        except ValueError:
                            pass
                    else :
                        planete2.agglo(planete1)
                        try: 
                            Planetes.remove(planete1)
                        except ValueError:
                            pass
            planete1.pos += planete1.v
            
            canvas.create_oval(planete1.pos[0] - planete1.r, planete1.pos[1] - planete1.r, planete1.pos[0] + planete1.r, planete1.pos[1] + planete1.r, fill = 'yellow')
            planete1.draw_trajectory(canvas)
            planete1.Pool_boundary(canvas, False)
            
            sumpos += planete1.pos*planete1.m
            summ += planete1.m
    else:
        methode = 'Natural method'
        for planete1 in Planetes:
            for planete2 in Planetes:
                if np.linalg.norm(planete1.pos-planete2.pos):
                    planete1.Fg(planete2)
                if np.linalg.norm(planete1.pos-planete2.pos) < (planete1.r + planete2.r) and planete1 != planete2:
                    if planete1.m > planete2.m:
                        planete1.agglo(planete2)
                        try:
                            Planetes.remove(planete2)
                        except ValueError:
                            pass
                    else :
                        planete2.agglo(planete1)
                        try: 
                            Planetes.remove(planete1)
                        except ValueError:
                            pass
            planete1.pos += planete1.v
            
            canvas.create_oval(planete1.pos[0] - planete1.r, planete1.pos[1] - planete1.r, planete1.pos[0] + planete1.r, planete1.pos[1] + planete1.r, fill = 'yellow')
            planete1.draw_trajectory(canvas)
            planete1.Pool_boundary(canvas, False)
            
            sumpos += planete1.pos*planete1.m
            summ += planete1.m

    
    barycentre = sumpos/summ
    canvas.create_text(barycentre[0], barycentre[1], text = "+", fill = 'white', anchor = NW)
    canvas.create_text(50, 40, text = "Time: "+str(round(T/fps,2)), fill = 'white', anchor = W)
    canvas.create_text(50, 20, text = "Nb planetes: "+str(round(len(Planetes),2)), fill = 'white', anchor = W)
    canvas.create_text(50, 60, text = methode, fill = 'white', anchor = W)

    canvas.update()
    time.sleep(1/fps)
    if T/fps>=100 or len(Planetes)==1:
        Tx=False