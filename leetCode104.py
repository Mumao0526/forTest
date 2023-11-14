# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # DFS
        visited = list()
        stack = list()
        visited.append(root)
        stack.append(root)
        nodelist = [root.val]

        while stack:
            if len(stack) >= 2:
                node = stack.pop(-2)
            else:
                node = stack.pop()
            #print(node.val ," has be trace.")

            if node.left and node.left not in visited:
                visited.append(node.left)
                stack.append(node.left)
                nodelist.append(node.left.val)
            else:
                nodelist.append('null')

            if node.right and node.right not in visited:
                visited.append(node.right)
                stack.append(node.right)
                nodelist.append(node.right.val)
            else:
                nodelist.append('null')

        while nodelist[-1] == 'null':
            nodelist.pop()
        print(nodelist)
        deep = round(log(len(nodelist) + 1, 2))
        print(log(len(nodelist) + 1, 2))
        return deep






