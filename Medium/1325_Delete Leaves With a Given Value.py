class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postorder(root, target):
            if root==None: return None
            
            root.left=postorder(root.left, target)
            root.right=postorder(root.right, target)

            if root.left==root.right and root.val==target:
                return None
            return root
            
        return postorder(root, target)
