#144. Binary Tree Preorder Traversal

class treenode:
    def __init__(self, val=0, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(self, root: treenode) -> list[int]:
    if not root: return []
    stack, ans = [root], []

    while stack:
        node = stack.pop()
        ans.append(node.val)
        print(node)
        if node.right :
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return ans

print(preorderTraversal(5,[1,2,3]))