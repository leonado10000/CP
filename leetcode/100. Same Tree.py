#100. Same Tree
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    stack = [[p,q]]# even pe left || odd pe right
    while( stack ):
        p,q = stack.pop()
        if not p and not q:
            continue
        elif p and q and p.val == q.val:
            stack.append([p.left,q.left])
            stack.append([p.right,q.right])
        else:
            return False
    return True