from rasterMap import *
from timeit import default_timer as timer

a = rasterMap()
a.import_image("cookie_3846-10.png")
#print(a.r)
#print(a.r.shape, a.g.shape)
#print(logical_and(a.r==0., a.g==0.))
#print(where(a.r == 0, True, False))
#print(a.img[500,0,:])
#a.image_show()
a.image_extract_color()
a.image_greyscale()
print(a.greyscale[int(a.nx/2), int(a.ny/2)])
start = timer()
a.image_setConstantH(color=[0,0,0,0], h=-1)
print(timer()-start)
a.set_h_from_greyscale()
#print(a.const_h[int(a.nx/2),:])
print(a.const_h)
