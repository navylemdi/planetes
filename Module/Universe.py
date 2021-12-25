from Module.planete import *
import random as random
import numpy as np

class Universe():
    def __init__(self, G, screensize, Boundary_type, Nbplanete, Circular=False, diffusive = False):
        self.G = G
        self.screensize = screensize
        self.Boundary = Boundary_type
        self.Nbplanete = Nbplanete
        self.Planetes = []
        self.Sun = False
        self.Circular = Circular
        self.diffusive = diffusive

    def create_planetes(self):
        if self.Sun:
            for i in range(self.Nbplanete):
                if self.Circular:
                    theta = random.randrange(0,360)
                    rh = random.randrange(100,int(self.screensize[1]/2)+1)
                    posx = rh*np.cos(theta/360*2*np.pi)+self.screensize[0]/2
                    posy = rh*np.sin(theta/360*2*np.pi)+self.screensize[1]/2
                    inv = random.randrange(0,2)
                    vx = np.sqrt(self.G*self.Planetes[0].m/rh)*np.cos(theta/360*2*np.pi + np.pi/2)
                    vy = np.sqrt(self.G*self.Planetes[0].m/rh)*np.sin(theta/360*2*np.pi + np.pi/2)
                if not self.Circular:
                    posx = random.randrange(0,self.screensize[0]+1)
                    posy = random.randrange(0,self.screensize[1]+1)
                    vx = random.randrange(-5,5+1)/5
                    vy = random.randrange(-5,5+1)/5
                r = random.random()+1
                self.Planetes.append(planete(np.array([posx, posy], dtype=float), np.array([vx, vy], dtype=float), r))
        else:
            for i in range(1, self.Nbplanete):
                if self.Circular:
                    theta = random.randrange(0,360)
                    rh = random.randrange(100,int(self.screensize[1]/2)+1)
                    posx = rh*np.cos(theta/360*2*np.pi)+self.screensize[0]/2
                    posy = rh*np.sin(theta/360*2*np.pi)+self.screensize[1]/2
                    inv = random.randrange(0,2)
                    vx = np.sqrt(self.G*self.Planetes[0].m/rh)*np.cos(theta/360*2*np.pi + np.pi/2)
                    vy = np.sqrt(self.G*self.Planetes[0].m/rh)*np.sin(theta/360*2*np.pi + np.pi/2)
                if not self.Circular:
                    posx = random.randrange(0,self.screensize[0]+1)
                    posy = random.randrange(0,self.screensize[1]+1)
                    vx = random.randrange(-5,5+1)/5
                    vy = random.randrange(-5,5+1)/5
                r = random.random()+1
                self.Planetes.append(planete(np.array([posx, posy], dtype=float), np.array([vx, vy], dtype=float), r))
        
    def create_sun(self, mass):
        self.Planetes.append(planete(np.array([self.screensize[0]/2, self.screensize[1]/2], dtype=float), np.array([0, 0], dtype=float), m = mass))
        self.Sun = True
        