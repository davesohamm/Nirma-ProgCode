# 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-1 "Tree: Inorder Traversal"
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
