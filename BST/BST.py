class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
# func to print the right view
def rightViewUtil(root,level,max_level):
    if root is None:
        return
    # if this is the first node
    # of its level
    if(max_level[0]<level):
        print(root.key,end=" ")
        max_level[0]=level
    #recur for right and leftt subtrees
    rightViewUtil(root.right,level+1,max_level)
    rightViewUtil(root.left,level+1,max_level)


def leftViewUtil(root,level,max_level):
    if root is None:
        return
#     if this is the 1st node
    if(max_level[0]<level):
        print(root.key,end=" ")
        max_level[0]=level
#     recur from left to right subtrees
    leftViewUtil(root.left,level+1,max_level)
    leftViewUtil(root.left,level+1,max_level)

# Wrapper over leftViewUtil()
def leftView(root):
    max_level=[0]
    leftViewUtil(root,1,max_level)
def rightView(root):
    max_level=[0]
    rightViewUtil(root,1,max_level)

# Get height of the BST
def height(node):
    if node is None:
        return 0
    else:
        lDepth=height(node.left)
        rDepth=height(node.right)

    #use the larger one
    if lDepth<rDepth:
        return (rDepth+1)
    else:
        return (lDepth+1)

# delete a node from the BST
def deleteNode(root,key):
#     base case
    if root is None:
        return root
    #if key to be deleted is
    # smaller than the root's key
    # then it lies in the left subtree
    if key<root.key:
        root.left=deleteNode(root.left,key)
    # if key to be deleted is
    # greater than the root's key
    # then it lies in the right subtree
    elif key < root.key:
        root.right = deleteNode(root.left, key)
    #if key is same as the root key
    #then its the key to be delted
    #
    else:
        #node with only child
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        #Node with 2 children
        # Get the inorder successor(smallest)
        # in the right subtee
        temp=minValueNode(root.right)
        #copy the inorder successor's
        #content to this node
        root.key=temp.key
    # `   delete the inorder successor
        root.right=deleteNode(root.right,temp.key)
def minValuedNode(node):
    current=node
#     loop down to find the leftmost leaf
    while current and current.left is not None:
        current=current.left
    return current
# total number of node in a BST
# FUNCTION TO CREATE A NEWNODE
def newNode(item):
    temp=Node(item)
    return  temp
# node count method
def nodeCount(node):
    if node is None:
        return 0
    else:
        return nodeCount(node.left)+nodeCount(node.right)+1
# delete entire BST
def emptyBST(root):
    if root is not None:
        emptyBST(root.left)
        emptyBST(root.right)
        print("\nReleased node",root.key)
        #require for free memory
        del root
if __name__ =="__main__":
    root=None
    root=insert(root,50)
    insert(root,30)
    insert(root, 70)
    insert(root, 20)
    insert(root, 40)
    insert(root, 60)
    insert(root,80)
    rightView(root)
    print()
    print("Height of the tree:",height(root))
    print("Nodes in count BST",nodeCount(root))
    leftView(root)
    # delete the bst
    root=emptyBST(root)
    print("Nodes in count BST after emptyBST():", nodeCount(root))


