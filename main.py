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
NbPlanetes = 200
fps = 60
# Masse = [1.989e30, 3.285e23, 4.867e24, 5.972e24,  6.39e23]#kg
# Rayon = [20, 0.38*10, 0.9497*10, 1*10, 0.53*10]
# pos=[0, 61.741e6, 107.74e6, 147.15e6, 232.93e6]*1000 #m
# theta = [0, 317, 81, 91, 231]#deg
# vr = [0, -8.73, -0.18, -0.09, -2.18]*1000 #m/s
# def convert_distance(value):
#     return value*width/pos[-1]

#Planetes.append(planete(np.array([width/2, height/2], dtype=float), np.array([0, 0], dtype=float),10, 100))
for i in range(0, NbPlanetes):
    posx = random.randrange(0,width)
    posy = random.randrange(0,height)
    vx = random.randrange(-5,5)
    vy = random.randrange(-5,5)
    r = random.randrange(1,2)
    Planetes.append(planete(np.array([posx, posy], dtype=float), np.array([vx, vy], dtype=float), r))
T = 0
Tx = True
ENERGY = []
while Tx == True:
    T+=1
    canvas.delete('all')
    Energy = 0
    for planete1 in Planetes:
        
        for planete2 in Planetes:
            planete1.Fg(planete2)

            if np.linalg.norm(planete1.pos-planete2.pos) < (planete1.r + planete2.r) and planete1 != planete2:
                if planete1.m > planete2.m:
                    planete1.agglo(planete2)
                    Planetes.remove(planete2)
                else :
                    planete2.agglo(planete1)
                    Planetes.remove(planete1)
    
        planete1.pos += planete1.v
        planete1.update_radius()
        canvas.create_oval(planete1.pos[0] - planete1.r, planete1.pos[1] - planete1.r, planete1.pos[0] + planete1.r, planete1.pos[1] + planete1.r, fill = 'yellow')
        planete1.draw_trajectory(canvas, planete1.Tore_boundary(canvas, False))
    Energy += 0.5 * np.linalg.norm(planete1.v)**2 * planete1.m
    ENERGY.append(Energy)
    canvas.create_text(50, 20, text = "Cinetic energy: "+str(round(Energy,2)), fill = 'white', anchor = W)
    canvas.create_text(50, 50, text = "Time: "+str(round(T/fps,2)), fill = 'white', anchor = W)
    canvas.create_text(50, 80, text = "Nb planetes: "+str(round(len(Planetes),2)), fill = 'white', anchor = W)
    canvas.update()
    time.sleep(1/fps)

    if T/fps>=100 or len(Planetes)==1:
        Tx=False


plt.figure()
plt.plot([i/fps for i in range(len(ENERGY))],ENERGY)
plt.title('Cinetic energy vs time')
plt.xlabel('Time (s)')
plt.ylabel('Cinetic energy')
plt.grid()
plt.show()