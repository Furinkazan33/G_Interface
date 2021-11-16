import uuid


def t_new(name: str, info: any):
    return (uuid.uuid4(), name, info, [])

def t_add(children: list, to_node):
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

# Recc moving the corresponding nodes at the beginning
def touch(ids: list, nodes: list):
    if not ids:
        return []
        
    id = ids.pop(0)
    
    for i, node in enumerate(nodes):
        (uid, name, info, children) = node
        
        if id == uid:
            nodes.insert(0, nodes.pop(i))
            touch(ids, children)
    

