from Tree import *
import uuid


def gt_new(name: str, context):
    return t_new(name, context)

def gt_add(children: list, to_node):
    return t_add(children, to_node)

# Coordinates matches context
def gt_match(x: int, y: int, context):
    (xc, yc, w, h) = context
    return xc < x and x < xc + w and yc < y and y < yc + h

# Liste des identifiants depuis ROOT
def gt_find_branch_by_coord(x: int, y: int, nodes: list):
    for node in nodes:
        (id, name, context, children) = node
        if gt_match(x, y, context):
            return [id] + gt_find_branch_by_coord(x, y, children)
            
    return []
