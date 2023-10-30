#create a node and insert inot a BST
class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    elif key>node.key:
        node.right=insert(node.right,key)
    return node
# Function to do inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

# preorder traversal of the tree
def preOrder(root):
    if root:
        print(root.key,end=" ")
        preOrder(root.left)
        preOrder(root.right)
# return height of tree
def height(node):
    if node is None:
        return 0
    else:
        lDepth=height(node.left)
        rDepth=height(node.right)

#         use the larger one
        if rDepth<lDepth:
            return (lDepth+1)
        else:
            return (rDepth+1)

#     print the givenLevelNOde
def printGivenLevel(root,level):
    if root is None:
        return
    if level==1:
        print(root.key,end=" ")
    elif level>1:
#         recursive call
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)

# print the levelOrder
def printLevelOrder(root):
    h=height(root)
    for i in range(1,h+1):
        printGivenLevel(root,i)
        print()
# driver code
def printLeafNodes(root):
    if not root:
        return
# if node is leaf node
    if not root.left and not root.right:
       print(root.key,end=" ")
   # if left child exist
   #check for leaf recursively
    if root.left:
       printLeafNodes(root.left)
    if root.right:
       printLeafNodes(root.right)

def printNonLeafNode(root):
    if not root or(not root.left and not root.right):
        return
    if root.left is not None or root.right is not None:
        print(root.key,end=" ")
    printNonLeafNode(root.right)
    printNonLeafNode(root.left)
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
        temp=minValuedNode(root.right)
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

if __name__ =='__main__':
    root=None
    root=insert(root,50)
    insert(root,30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 80)
    insert(root, 60)
    insert(root, 60)

    # print BST
    print('Inorder tree traversal')
    inorder(root)
    print("Preorder Traversal")
    preOrder(root)
    print("LevelOrder Traversal")
    printLevelOrder(root)
    print("PRINT AT LEVEL 2")
    printGivenLevel(root,2)

    print("Print the leaf nodes")
    printLeafNodes(root)

    print("Printing none leaf nodes")
    printNonLeafNode(root)
    print()
    print("LevelOrder Traversal before deleting the root")
    printLevelOrder(root)
    deleteNode(root,50)
    print("LevelOrder Traversal after deleting the root")
    printLevelOrder(root)