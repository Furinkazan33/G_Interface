import uuid


def t_new(name, info):
    return (uuid.uuid4(), name, info, [])

def t_add(children, to_node):
    (uid, name, info, chldn) = to_node
    return (uid, name, info, children + chldn)

def get_uid(node):
    (uid, name, info, children) = node
    return uid

def get_name(node):
    (uid, name, info, children) = node
    return name

def get_info(node):
    (uid, name, info, children) = node
    return info

def get_children(node):
    (uid, name, info, children) = node
    return children


def touch(node, tree):
    id = get_uid(get_children(node)[0])
    child = get_children(node)[0]
    
    (uid, name, info, children) = tree
    
    for c, i in children:
        if id == get_uid(c):
            children.pop(i)
            return (uid, name, info, touch(child, c) + children)

    return [c]



