def treap_merge(a, b):
    if a == None or b == None:
        return a or b
    if a.priority > b.priority:
        return a.update(right=treap_merge(a.right, b))
    else:
        return b.update(left=treap_merge(a, b.left))
