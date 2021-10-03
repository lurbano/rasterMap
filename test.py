from rasterMap import *
from timeit import default_timer as timer

outstep = 10

a = rasterMap(100,100, center=True)
a.h[6] = 2

a.const_h[4,4] = 2

#a.draw_boxes()
a.draw_heatmap()

for i in range(100):
    start = timer()
    a.diffuse()
    #a.redraw_boxes()
    sleep(0.01)

    if i%outstep == 0:
        a.update_heatmap()
    step_dt = start - timer()
    print(i, step_dt)
    #print(i, end="\r", flush=True)

a.update_heatmap(final=True)
