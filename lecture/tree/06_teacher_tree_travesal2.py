left = [None] * 16
right = [None] * 16

left[1] = 2
right[1] = 3
left[2] = 4
left[3] = 6
right[3] = 7
left[6] = 12
right[6] = 13


def preorder(v):
    if v is None:
        return
    print(v, end=' ')
    preorder(left[v])
    preorder(right[v])

preorder(1)
# 1 2 4 3 6 12 13 7 

print()

def inorder(v):
    if v is None: 
        return
    inorder(left[v])
    print(v, end=' ')
    inorder(right[v])

inorder(1)
# 4 2 1 12 6 13 3 7 

print()

def postorder(v):
    if v is None: 
        return
    postorder(left[v])
    postorder(right[v])
    print(v, end=' ')

postorder(1)
# 4 2 12 13 6 7 3 1

