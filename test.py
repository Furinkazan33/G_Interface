from G_Interface import *

canvas_init(250, 500)


w1 = w_new("w1", (10, 10, 50, 80))
w2 = w_new("w2", (50, 50, 250, 200))
w21 = w_new("w21", (60, 60, 200, 150))
w2 = w_add([w21], w2)

canvas_add([w1, w2])

mainloop()


