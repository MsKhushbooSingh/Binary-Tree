# Python program to find largest   BST in a Binary Tree. 
  
minVal= -2147483648
maxVal = 2147483647
  
# Helper function that allocates a new node with the given data and None left and right pointers.  
class newNode:  
  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
  
# Returns Information about subtree which includes size of largest subtree which is a BST 
def largestBSTBT(root): 
      
# Base cases : When tree is empty or it has  
    # one child.  
    if (root == None): 
        return 0, minVal, maxVal, 0, True
    if (root.left == None and root.right == None) : 
        return 1, root.data, root.data, 1, True
  
    # Recur for left subtree and right subtrees  
    l = largestBSTBT(root.left)  
    r = largestBSTBT(root.right)  
  
    # Create a return variable and initialize its size.  
    ret = [0, 0, 0, 0, 0]  
    ret[0] = (1 + l[0] + r[0])  
  
    # If whole tree rooted under current root is  BST.  
    if (l[4] and r[4] and l[1] <  
        root.data and r[2] > root.data) : 
      
        ret[2] = min(l[2], min(r[2], root.data))  
        ret[1] = max(r[1], max(l[1], root.data))  
  
        # Update answer for tree rooted under  
        # current 'root'  
        ret[3] = ret[0]  
        ret[4] = True
  
        return ret  
      
  
    # If whole tree is not BST, return maximum  
    # of left and right subtrees  
    ret[3] = max(l[3], r[3])  
    ret[4] = False
  
    return ret 
  
# Driver Code  
if __name__ == '__main__':  
      
    """Let us construct the following Tree 
        20 
        / \  
        25 30  
    /  
    10 """
    root = newNode(20)  
    root.left = newNode(25)  
    root.right = newNode(30)  
    root.left.left = newNode(10) 
    print("Size of the largest BST is",largestBSTBT(root)[3])  
                              
