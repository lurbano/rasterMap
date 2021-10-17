from vpython import *
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class rasterMap:
    def __init__(self, nx=10, ny=10, dx=1.0, center=True):
        self.setup(nx, ny, dx, center)

    def setup(self, nx, ny, dx=1.0, center=True):
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


    def draw_boxes(self, const_h_color = vec(1,1,1)):
        self.boxes = []
        for i in range(self.nx):
            self.boxes.append([])
            y = -i * self.dx - self.offset.x
            #print(i, self.dx, self.offset.x)
            for j in range(self.ny):
                x = j * self.dx + self.offset.y
                z = self.h[i, j]
                self.boxes[-1].append(box(pos=vec(x, y, z), length=self.dx, width=self.dx))
                if self.const_h[i, j] != 0:
                    self.boxes[-1][-1].color = const_h_color

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

    def update_heatmap(self, final=False):
        self.heatmap.set_data(self.h)
        if final:
            plt.show()
        else:
            plt.draw(), plt.pause(1e-3)

    def set_constant_h_cells(self):
        self.h = where(self.const_h, self.const_h, self.h)

#### IMAGES (start)
    def import_image(self, fname):
        # image should be rgba
        # by default we'll set the constant head to the a channel:
        try:
            self.img = mpimg.imread(fname)
            self.r = self.img[:,:,0]
            self.g = self.img[:,:,1]
            self.b = self.img[:,:,2]
            self.a = self.img[:,:,3]
            (nx, ny, nz) = self.img.shape
            (self.nx, self.ny) = (nx, ny)
            self.setup(nx, ny)
        except:
            print("Failed to import:", fname)
            die

    def image_show(self, img=None, greyscale=False):
        try:
            if img == None:
                img = self.img
        except:
            print("trying")

        if not greyscale:
            self.imgplot = plt.imshow(img)
        else:
            self.imgplot = plt.imshow(self.greyscale, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
        plt.show()

    def image_extract_color(self, color=1):
        print(self.img[:,:,1].shape)

    def image_setConstantH(self, color=[0,0,0,0], h = 9):
        t = logical_and(self.r == color[0], self.g == color[1])
        #print("t1", t)
        t = logical_and(t, self.b == color[2])
        #print("t2", t)
        t = logical_and(t, self.a == color[3])
        #print("t3", t)
        self.const_h = self.const_h + t*h
        #print("const_h", self.const_h)
        # a = self.img
        # self.const_h = where(array_equal(a, color), a/a+h, a*0)
        # for i in range(self.nx):
        #     for j in range(self.ny):
        #         # if self.img[i,j,3] == 1:
        #         # print(self.img[i,j,:], array_equal(self.img[i,j,:], color))
        #         if array_equal(self.img[i,j,:], color):
        #             #print(i,j)
        #             self.const_h[i,j] = h


    def image_greyscale(self, show=False):
        self.greyscale = dot(self.img[...,:3], [0.2989, 0.5870, 0.1140])
        print(self.greyscale)
        if show:
            plt.imshow(self.greyscale, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
            plt.show()

    def set_h_from_greyscale(self, h_scale=10):
        self.h = self.greyscale * h_scale
        self.set_constant_h_cells()

    def image_save(self, fname, data, greyscale=False):
        if greyscale:
            plt.imsave(fname, data, cmap=plt.get_cmap('gray'), vmin=0, vmax=10)
        else:
            plt.imsave(fname, data)


#### IMAGES (end)
