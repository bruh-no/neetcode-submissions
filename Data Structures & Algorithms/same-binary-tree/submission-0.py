# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        que = deque()

        que.append(p)
        que.append(q)

        while que:
            r = que.pop()
            l = que.pop()

            # check that r and l are BOTH real before checking vals

            if r is None and l is None:
                continue
            
            if r is None or l is None:
                return False
            
            # check vals and append next nodes

            else:
                if r.val != l.val:
                    return False
                
                que.append(l.right)
                que.append(r.right)
                que.append(l.left)
                que.append(r.left)
                
        
        return True
            



        