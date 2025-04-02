def inorder(root, s):
    if root: inorder(root.left, s); s.add(root.key); inorder(root.right, s)

def countPairs(root1, root2, x):
    s, count = set(), 0
    inorder(root1, s)
    def findPairs(root):
        nonlocal count
        if root:
            findPairs(root.left)
            count += (x - root.key in s)
            findPairs(root.right)
    findPairs(root2)
    return count

root1, root2 = Node(5), Node(10)
root1.left, root1.right = Node(3), Node(7)
root1.left.left, root1.left.right = Node(2), Node(4)
root2.left, root2.right = Node(6), Node(15)
root2.left.left, root2.left.right = Node(3), Node(8)

print("Count of pairs:", countPairs(root1, root2, 11))
