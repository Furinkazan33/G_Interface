from tkinter import *
from G_Tree import *


root = Tk()
canvas = Canvas()
w_root = ()


def w_new(name: str, context):
    return gt_new(name, context)


def w_add(children: list, to_node):
    return gt_add(children, to_node)


def canvas_init(h: int, w: int):
    global canvas, w_root

    canvas = Canvas(root, height=h, width=w)
    canvas.pack()
    
    w_root = w_new("ROOT", (0, 0, w, h))

    # Bindings
    canvas.bind('<Button-1>', click)


def canvas_add(children: list):
    global w_root
    #print('{}'.format(w_root))
    w_root = w_add(children, w_root)
    draw()
    

def draw():
    _draw(w_root)


# Draw widget and all children
def _draw(widget):
    (id, name, context, c) = widget
    (x, y, w, h) = context

    canvas.create_rectangle(x, y, x + w, y + h, fill='green')
    # TODO: save image inside widget

    for w in reversed(c):
        _draw(w)


#def click(event):
    # find widget clicked, marke it as clicked and 
    # move its branch to the beginning


#def move(event):
    # if widget marked as clicked, draw image every delta

    
#def release(event):
    # If widget marked as clicked, move it to the release position
    # unmark it as clicked
    # redraw screen if needed



def click(event):
    global w_root
    x, y = event.x, event.y

    # Liste des identifiants depuis ROOT
    ids = gt_find_branch_by_coord(x, y, [w_root])
    #print('{}'.format(ids))

    # Move the clicked branch at the beginning
    touch(ids, [w_root])
    print('{}'.format(w_root))

    # Refresh canvas
    canvas.delete("all")
    draw()


def mainloop():
    root.mainloop()

