from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    # Leaf node: does the remaining sum match this node's value?
    if not root.left and not root.right:
        return root.val == targetSum

    remaining = targetSum - root.val
    return hasPathSum(root.left, remaining) or hasPathSum(root.right, remaining)


root = TreeNode(5,
    TreeNode(4,
        TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8,
        TreeNode(13),
        TreeNode(4, None, TreeNode(1))))

print(hasPathSum(root, 22))  # True  (5 -> 4 -> 11 -> 2)
