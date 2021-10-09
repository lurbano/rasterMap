from rasterMap import *
from timeit import default_timer as timer
import time

a = rasterMap()
a.import_image("cookie_3846-10b.png")
#print(a.r)
print(a.g, a.g.shape)
#print(logical_and(a.r==0., a.g==0.))
#print(where(a.r == 0, True, False))
#print(a.img[500,0,:])
#a.image_show()
a.image_extract_color()
a.image_greyscale()
print(a.greyscale[int(a.nx/2), int(a.ny/2)])
start = timer()
#a.image_setConstantH(color=[0,0,0,0], h=-1)
a.image_setConstantH(color=[0,1,0,1], h=5)
print("timer", timer()-start)
a.set_h_from_greyscale()
#print(a.const_h[int(a.nx/2),:])
print(a.h)
a.draw_boxes()


for i in range(100):
    a.diffuse(K=100)
    time.sleep(0.1)
    print(i)
