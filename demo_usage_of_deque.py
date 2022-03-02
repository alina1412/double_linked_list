# LeetCode 102. Binary Tree Level Order Traversal

from typing import List, Optional
import leetcode.tree as tree
# from collections import deque
from mycollections import deque


class Solution:
    def levelOrder(self, root: Optional[tree.TreeNode]) -> List[List[int]]:
        ans = []
        que = deque([root])  # [<><><15><7>]
        while que:
            n = len(que)  # 4
            lvl = []  # []
            for i in range(n):
                node = que.popleft()  # <20>
                if node:
                    lvl.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if lvl:
                ans.append(lvl)
        return ans  # [ [3], [9,20] ]


sol = Solution()
par = tree.stringToTreeNode("[3,9,20,null,null,15,7]")
tree.prettyPrintTree(par)
ans = sol.levelOrder(par)
print(ans)
