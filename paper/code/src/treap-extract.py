def extract_fringe(node, side):
    if node == None:
        return None
    if side == 'left':
        return node.update(left=extract_fringe(node.left, 'left'), 
                           right=hash(node.right)).
    elif side == 'right':
        return node.update(left=hash(node.left),
                           right=extract_fringe(node.right, 'right'))
    else: # root
        return node.update(left=extract_fringe(node.left, 'left'),
                           right=extract_fringe(node.right, 'right'))
