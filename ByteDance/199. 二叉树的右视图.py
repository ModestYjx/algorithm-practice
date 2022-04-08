# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    resList = []
    root = TreeNode()
    root.val = 1
    root.left = None
    root.right = None

    def loopRight(self, root: TreeNode) -> List[int]:

        # if root is not None:
        #     self.resList.append(root.val)
        if root is None:
            return
        if root.val is not None:
            self.resList.append(root.val)
        # elif root.right is not None:
        #     self.resList.append(self.loopRight(root.right))
        # if root.right  is not None:
        #     self.loopRight(root.right)
        self.loopRight(root.right)

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.resList
        else:
            self.resList.append(root.val)
        workNode = root
        self.loopRight(workNode.right)
        return self.resList
        print(self.resList)