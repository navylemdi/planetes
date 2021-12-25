from Module.quadtree import *
import numpy as np

class Barnes_hut():
    def __init__(self, Planetes, qt, canvas, boundary, diffusive, draw_qt,draw_soi):
        self.Planetes = Planetes
        self.qt = qt
        self.canvas = canvas
        self.method = 'Barnes-hut method'
        self.summ = 0
        self.sumpos = 0
        for planete1 in Planetes:
            qt.insert(planete1)
            rect = Circle(planete1.pos[0], planete1.pos[1], 200)
            if draw_soi:
                canvas.create_oval(rect.x-rect.w, rect.y-rect.h, rect.x+rect.w, rect.y+rect.h, outline = 'green')
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

            if boundary == 'Pool':
                planete1.Pool_boundary(canvas, diffusive)
            if boundary == 'Tore':
                planete1.Tore_boundary(canvas, diffusive)
            if boundary == 'Sphere':
                planete1.Sphere_boundary(canvas, diffusive)
            self.sumpos += planete1.pos*planete1.m
            self.summ += planete1.m
            
            canvas.create_oval(planete1.pos[0] - planete1.r, planete1.pos[1] - planete1.r, planete1.pos[0] + planete1.r, planete1.pos[1] + planete1.r, fill = 'yellow')
            planete1.draw_trajectory(canvas)
            if draw_qt:
                qt.show(canvas)

