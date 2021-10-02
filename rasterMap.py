from vpython import *
from numpy import *

class rasterMap:
    def __init__(self, nx, ny, dx=1.0, center=True, baseLevel = 0.0):
        self.nx = nx
        self.ny = ny
        self.dx = dx
        self.data = ones((nx, ny))
        self.center = center
        self.baseLevel = baseLevel
        if center:
            self.offset = vector(-nx * dx / 2.0, -ny * dx / 2.0, 0)
        else:
            self.offset = vector(0,0,0)

    def draw_boxes(self):
        self.boxes = []
        for i in range(self.nx):
            self.boxes.append([])
            x = i * self.dx + self.offset.x
            #print(i, self.dx, self.offset.x)
            for j in range(self.ny):
                y = j * self.dx + self.offset.y
                h = self.data[i,j] - self.baseLevel
                z = h / 2.0  #self.data[i, j]
                self.boxes[-1].append(box(pos=vec(x, y, z), length=self.dx, width=h, height=self.dx))
                #print(x,y,z)

    def diffuse(self, K=1, dt=1, nsteps=1):
        for i in range(nsteps):
            self.data[1:-1] = q
