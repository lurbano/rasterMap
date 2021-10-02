from vpython import *
from numpy import *
import matplotlib.pyplot as plt

class rasterMap:
    def __init__(self, nx, ny, dx=1.0, center=True):
        self.nx = nx
        self.ny = ny
        self.dx = dx
        self.h = ones((nx, ny))
        self.const_h = zeros((nx, ny))

        self.center = center
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
                z = self.h[i, j]
                self.boxes[-1].append(box(pos=vec(x, y, z), length=self.dx, width=self.dx))
                #print(z)
                #print(x,y,z)

    def redraw_boxes(self):
        for i in range(self.nx):
            for j in range(self.ny):
                self.boxes[i][j].pos.z = self.h[i][j]

    def diffuse(self, K=0.01, dx = 1):
        h = self.h
        #print(self.nx, self.ny)
        self.h[1:self.nx-1, 1:self.ny-1] = h[1:self.nx-1, 1:self.ny-1]  + K* ((h[0:self.nx-2, 1:self.ny-1] - 2 * h[1:self.nx-1, 1:self.ny-1] + h[2:self.nx, 1:self.ny-1])/ dx**2 ) + K*((h[1:self.nx-1, 0:self.ny-2] - 2 * h[1:self.nx-1, 1:self.ny-1] + h[1:self.nx-1, 2:self.ny]) / dx**2)

        # reset constant h cells
        self.h = where(self.const_h, self.const_h, h)

    def draw_heatmap(self):
        self.heatmap = plt.imshow(self.h)
        plt.draw(), plt.pause(1e-3)
        #plt.show()

    def update_heatmap(self):
        self.heatmap.set_data(self.h)
        draw(), plt.pause(1e-3)
