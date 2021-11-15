from Tree import *
import uuid



def gt_new(name, context):
    return t_new(name, context)

def gt_add(children, to_node):
    return t_add(children, to_node)

# Coordinates matches context
def gt_match(x, y, context):
    (xc, yc, w, h) = context
    
    return xc < x and x < xc + w and yc < y and y < yc + h

# Find the corresponding branch
def gt_find_branch_by_coord(x, y, start_node):
    return _find_branch_by_coord(x, y, start_node, [])
    

def _find_branch_by_coord(x, y, start_node, result):
    (id, name, context, children) = start_node

    if gt_match(x, y, context):
        result += start_node

    for c in children:
        result += _find_branch_by_coord(x, y, c, result)

    return result

