import numpy as np

class planete():
    def __init__(self, pos, v, r, m = 1):
        self.pos = pos
        self.v = v
        self.r = r
        if m == 1:    
            self.m = np.pi*(self.r)**2
        else:
            self.m=m
        self.G = 1
        self.path=[]
        self.cross_boundary = False

    def Fg(self, other):
        if self==other:
            self.dv = np.array([0,0], dtype = float)
        else:
            self.d = np.linalg.norm(self.pos-other.pos)
            vectuni = (self.pos-other.pos)/self.d
            self.fg = -(self.G*self.m*other.m/(self.d**2+1e-1)) * vectuni
            self.dv = self.fg/self.m
        self.v +=  self.dv
    
    def agglo(self, other):
        self.v = (self.m*self.v + other.m*other.v)/(self.m + other.m)
        self.m += other.m
        self.update_radius()
    
    def Tore_boundary(self, canvas, diffusive:bool):
        if self.pos[0] < 0:
            self.pos[0] = canvas.winfo_reqwidth()
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True
        if self.pos[0] > canvas.winfo_reqwidth():
            self.pos[0] = 0
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True
        if self.pos[1] < 0:
            self.pos[1] = canvas.winfo_reqheight()
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True
        if self.pos[1] > canvas.winfo_reqheight():
            self.pos[1] = 0
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True

    def Pool_boundary(self, canvas, diffusive:bool):
        if self.pos[0] < 0:
            self.v[0] *= -1
            if diffusive:
                self.v[0] *= 0.9
            self.cross_boundary = True
        if self.pos[0] > canvas.winfo_reqwidth():
            self.v[0] *= -1
            if diffusive:
                self.v[0] *= 0.9
            self.cross_boundary = True
        if self.pos[1] < 0:
            self.v[1] *= -1
            if diffusive:
                self.v[1] *= 0.9
            self.cross_boundary = True
        if self.pos[1] > canvas.winfo_reqheight():
            self.v[1] *= -1
            if diffusive:
                self.v[1] *= 0.9
            self.cross_boundary = True

    def Sphere_boundary(self, canvas, diffusive:bool):
        if self.pos[0] < 0:
            self.pos[0] = canvas.winfo_reqwidth()
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True
        if self.pos[0] > canvas.winfo_reqwidth():
            self.pos[0] = 0
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True
        if self.pos[1] < 0:
            self.pos[0] = canvas.winfo_reqwidth() - self.pos[0]
            self.pos[1] = 0
            self.v[1] *= -1
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True
        if self.pos[1] > canvas.winfo_reqheight():
            self.pos[0] = canvas.winfo_reqwidth() - self.pos[0]
            self.pos[1] = canvas.winfo_reqheight()
            self.v[1] *= -1 
            if diffusive:
                self.v *= 0.5
            self.cross_boundary = True

    def update_radius(self):
        self.r = np.sqrt(self.m/np.pi)

    def draw_trajectory(self, canvas):
        self.path.append([self.pos[0], self.pos[1]])
        if len(self.path)>10:
            self.path = self.path[1:] + self.path[:1]
            self.path.pop()
        if self.cross_boundary:
            self.path = []
            self.cross_boundary = False
        for i in range(len(self.path)-1):
            canvas.create_line(self.path[i][0], self.path[i][1], self.path[i+1][0], self.path[i+1][1], fill='white')
        

       

