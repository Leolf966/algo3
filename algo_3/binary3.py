class TreeNode:
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

root = TreeNode(10)
root.left = TreeNode(5)
root.left.parent = root
root.right = TreeNode(15)
root.right.parent = root
root.left.left = TreeNode(3)
root.left.left.parent = root.left
root.left.right = TreeNode(7)
root.left.right.parent = root.left
root.right.right = TreeNode(20)
root.right.right.parent = root.right
root.right.right.left = TreeNode(12)
root.right.right.left.parent = root.right.right

target_node = root.left.left 

successor = in_order_successor(root, target_node)

if successor:
    print("In-order successor of the target node is:", successor.value)
else:
    print("Target node does not have an in-order successor.")
