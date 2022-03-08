# The usage of the implementation of a `deque` container
# for the solution of the task of  Binary Tree level order traversal
# from the LeetCode site
# (https://leetcode.com/problems/binary-tree-level-order-traversal/)

from typing import List, Optional
import leetcode.tree as tree
# from collections import deque
from mycollections import deque


class Solution:
    def level_order_traversal(self, root: Optional[tree.TreeNode]) -> List[List[int]]:
        ans = []
        que = deque([root])
        while que:
            n = len(que)
            lvl = []
            for i in range(n):
                node = que.popleft()
                if node:
                    lvl.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if lvl:
                ans.append(lvl)
        return ans          # [[3], [9, 20], [15, 7]]


sol = Solution()
parsed_tree = tree.stringToTreeNode("[3,9,20,null,null,15,7]")
tree.prettyPrintTree(parsed_tree)
ans = sol.level_order_traversal(parsed_tree)
print(ans)
