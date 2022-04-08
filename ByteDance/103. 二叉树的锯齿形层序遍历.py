import collections
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    depth = 1

    resList = []
    def pushIntoList(self, root: TreeNode, depth: int) -> List[List[int]]:
        layerList = []
        countPerLayer = 2 ** (depth - 1)
        while
        if depth % 2 == 0:



    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.pushIntoList(root, self.depth)
        collections.deque()


