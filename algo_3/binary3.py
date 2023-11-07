class Nodes:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_last_left_child(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

def in_order_successor(root, target):
    if not root or not target:
        return None
    
    if target.right:
        return find_last_left_child(target.right)
    
    if target.parent and target == target.parent.left:
        return target.parent

    while target.parent and target == target.parent.right:
        target = target.parent

    return target.parent

root = Nodes(10)
root.left = Nodes(5)
root.left.parent = root
root.right = Nodes(15)
root.right.parent = root
root.left.left = Nodes(3)
root.left.left.parent = root.left
root.left.right = Nodes(7)
root.left.right.parent = root.left
root.right.right = Nodes(20)
root.right.right.parent = root.right
root.right.right.left = Nodes(12)
root.right.right.left.parent = root.right.right

target_node = root.left.left 

successor = in_order_successor(root, target_node)

if successor:
    print("In-order successor of the target node - true :", successor.value)
else:
    print("Target have an in-order successor - false.")
