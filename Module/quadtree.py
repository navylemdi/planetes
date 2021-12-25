class point():
    def __init__(self, planete):
        self.x = planete.pos[0]
        self.y = planete.pos[1]
        self.userdata = planete

class rectangle():
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return (point.x >= self.x-self.w and 
                point.x <= self.x+self.w and 
                point.y >= self.y-self.h and 
                point.y <= self.y+self.h)

    def intersects(self, range):
        return not (range.x-range.w > self.x+self.w or
                range.x+range.w < self.x-self.w or 
                range.y-range.h > self.y+self.h or 
                range.y+range.h < self.y-self.h)

class Circle():
    def __init__(self, x, y, w, h=1):
        self.x = x 
        self.y = y
        self.w = w
        self.h = w

    def contains(self, point):
        return (point.x >= self.x-self.w and 
                point.x <= self.x+self.w and 
                point.y >= self.y-self.h and 
                point.y <= self.y+self.h)

    def intersects(self, range):
        return not (range.x-range.w > self.x+self.w or
                range.x+range.w < self.x-self.w or 
                range.y-range.h > self.y+self.h or 
                range.y+range.h < self.y-self.h)

class quadtree():
    def __init__(self, boundary, n):
        self.boundary = boundary
        self.capacity = n
        self.point = []
        self.divided = False

    def insert(self, planete):
        if not self.boundary.contains(point(planete)):
            return False

        if len(self.point) < self.capacity:
            self.point.append(point(planete))
            return True 
        else:
            if not self.divided:
                self.subdivide()
            if self.ne.insert(planete):
                return True
            elif self.nw.insert(planete):
                return True
            elif self.se.insert(planete):
                return True
            elif self.sw.insert(planete):
                return True
    
    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        northeast = rectangle(x+w/2, y-h/2, w/2, h/2)
        self.ne = quadtree(northeast, self.capacity)
        northwest = rectangle(x-w/2, y-h/2, w/2, h/2)
        self.nw = quadtree(northwest, self.capacity)
        southeast = rectangle(x+w/2, y+h/2, w/2, h/2)
        self.se = quadtree(southeast, self.capacity)
        southwest = rectangle(x-w/2, y+h/2, w/2, h/2)
        self.sw = quadtree(southwest, self.capacity)
        self.divided = True

    def show(self, canvas):
        canvas.create_rectangle(self.boundary.x-self.boundary.w, self.boundary.y-self.boundary.h, self.boundary.x + self.boundary.w, self.boundary.y + self.boundary.h, outline = 'white')
        if self.divided:
            self.ne.show(canvas)
            self.nw.show(canvas)
            self.se.show(canvas)
            self.sw.show(canvas)
    
    def query(self, rect, found=None):
        if found == None:
            found = []
        if not self.boundary.intersects(rect):
            return
        else:
            for p in self.point:
                if rect.contains(p):
                    found.append(p)

            if self.divided:
                self.ne.query(rect, found)
                self.nw.query(rect, found)
                self.se.query(rect, found)
                self.sw.query(rect, found)

        return found
         
