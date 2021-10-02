from rasterMapB import *

a = rasterMap(10,10, center=True)
a.h[6] = 2

a.const_h[4,4] = 2

#a.draw_boxes()

for i in range(100):
    a.diffuse()
    #a.redraw_boxes()
    sleep(0.1)
    print(i, end="\r", flush=True)

    a.draw_heatmap()
