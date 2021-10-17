from rasterMap import *
from timeit import default_timer as timer
import time

a = rasterMap()
a.import_image("cookie_3846-100v.png")

l_boxes = False

#print(a.r)
print(a.g, a.g.shape)
#print(logical_and(a.r==0., a.g==0.))
#print(where(a.r == 0, True, False))
#print(a.img[500,0,:])
#a.image_show()
a.image_extract_color()
a.image_greyscale()
#a.image_show(a.greyscale, greyscale=True)
#print(a.greyscale[int(a.nx/2), int(a.ny/2)])
start = timer()
a.image_setConstantH(color=[0,1,0,1], h= 10)
a.image_setConstantH(color=[0,0,0,0], h=1)
print("timer", timer()-start)
a.set_h_from_greyscale()
a.draw_heatmap()
#print(a.const_h[int(a.nx/2),:])
# print("h", a.h)
# print("const_h:", a.const_h)
if l_boxes:
    a.draw_boxes(const_h_color=vec(1,1,0))
scene.forward = vec(0,1,-1)


for i in range(200):
    a.diffuse(K=0.01)
    if (i+1)%10 == 0:
        print(i+1)
        if l_boxes:
            a.redraw_boxes()
        a.update_heatmap()
    time.sleep(0.1)

a.image_save("out.png", a.h)
a.image_save("out_g.png", a.h, greyscale=True)
print("h", a.h)
