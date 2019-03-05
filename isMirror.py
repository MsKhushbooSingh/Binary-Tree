#Python code to check whether two trees are mirror of each other.

class newNode: 
    def __init__(self, data):  
        self.data = data  
        self.left = self.right = None

# function to check whether the two binary trees are mirrors of each other or not  
def areMirrors(root1, root2): 
    st1 = [] 
    st2 = [] 
    while (1): 
          
        #iterative inorder traversal of 1st tree and reverse inoder traversal of 2nd tree  
        while (root1 and root2): 
              
            # if the corresponding nodes in the two traversal have different data values, then they are not mirrors  of each other.  
            if (root1.data != root2.data):  
                return "No"
                  
            st1.append(root1)  
            st2.append(root2)  
            root1 = root1.left  
            root2 = root2.right 
          
        # if at any point one root becomes None and  the other root is not None, then they are not mirrors. This condition verifies that structures of tree are mirrors of each other.  
        if (not (root1 == None and root2 == None)):  
            return "No"
              
        if (not len(st1) == 0 and not len(st2) == 0): 
            root1 = st1[-1]  
            root2 = st2[-1]  
            st1.pop(-1)  
            st2.pop(-1)  
              
            # we have visited the node and its left subtree. Now, it's right subtree's turn  
            root1 = root1.right  
              
            # we have visited the node and its right subtree. Now, it's left subtree's turn  
            root2 = root2.left 
          
        # both the trees have been completely traversed  
        else: 
            break
      
    # tress are mirrors of each other  
    return "Yes"
  
# Driver Code 
if __name__ == '__main__': 
      
    # 1st binary tree formation  
    root1 = newNode(1)                             
    root1.left = newNode(3)        
    root1.right = newNode(2)  
    root1.right.left = newNode(5)
    root1.right.right = newNode(4) 
      
    # 2nd binary tree formation      
    root2 = newNode(1)                       
    root2.left = newNode(2)         
    root2.right = newNode(3) 
    root2.left.left = newNode(4)
    root2.left.right = newNode(5)
          
    print(areMirrors(root1, root2)) 
