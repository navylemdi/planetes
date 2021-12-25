from Module.quadtree import *
import numpy as np

class Natural_method():
    def __init__(self, Planetes, canvas, boundary, diffusive):
        self.Planetes = Planetes
        self.canvas = canvas
        self.summ = 0
        self.sumpos = 0
        self.method = 'Natural method'
        self.boundary = boundary
        self.diffusive = diffusive
        for planete1 in self.Planetes:
            for planete2 in self.Planetes:
                if np.linalg.norm(planete1.pos-planete2.pos):
                    planete1.Fg(planete2)
                if np.linalg.norm(planete1.pos-planete2.pos) < (planete1.r + planete2.r) and planete1 != planete2:
                    if planete1.m > planete2.m:
                        planete1.agglo(planete2)
                        try:
                            self.Planetes.remove(planete2)
                        except ValueError:
                            pass
                    else :
                        planete2.agglo(planete1)
                        try: 
                            self.Planetes.remove(planete1)
                        except ValueError:
                            pass
            planete1.pos += planete1.v
            
            if self.boundary == 'Pool':
                planete1.Pool_boundary(self.canvas, self.diffusive)
            if self.boundary == 'Tore':
                planete1.Tore_boundary(self.canvas, self.diffusive)
            if self.boundary == 'Sphere':
                planete1.Sphere_boundary(self.canvas, self.diffusive)
            self.sumpos += planete1.pos*planete1.m
            self.summ += planete1.m

            self.canvas.create_oval(planete1.pos[0] - planete1.r, planete1.pos[1] - planete1.r, planete1.pos[0] + planete1.r, planete1.pos[1] + planete1.r, fill = 'yellow')
            planete1.draw_trajectory(self.canvas)
            
