from rasterMap import *

a = rasterMap(20,10, center=True)
a.data[5][0] = 1.5
a.draw_boxes()
