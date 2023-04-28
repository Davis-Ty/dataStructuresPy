#object is a class and a object has functions 

class Node:
    #when a node is created it has the ability to let two nodes connect to it
    #it sets them to None starting off
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    #creating a binary tree and makes it the root then allows more nodes to connect to it
    def __init__(self, root):
        self.root = Node(root)

    #prints the tree out in specified order
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(self.root, "")
        
        elif traversal_type == "inorder":
            return self.inorder_traversal(self.root, "")
        
        elif traversal_type == "postorder":
            return self.postorder_traversal(self.root, "")
        
        else:
            print("Invalid traversal type.")
            return None

    #prints it in the order that the nodes came in
    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    #prints it so that the head is in the middle 
    #the true order of the tree
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    #prints it out where it starts at the node at the bottom left 
    #then prints left child right child
    #After finishing the starting .left nodes it starts at the node at the bottom right
    #then prints left child right child
    #prints the head last
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal
    
if __name__=='__main__':
        
    # Create a binary tree
    my_tree = BinaryTree(1)
    my_tree.root.left = Node(2)
    my_tree.root.left.left = Node(5)
    my_tree.root.left.right = Node(29)
    my_tree.root.right = Node(3)
    my_tree.root.right.right = Node(45)
    my_tree.root.right.left = Node(15)


    # Print the contents of the tree
    print("Preorder traversal:", my_tree.print_tree("preorder"))  
    print("Inorder traversal:", my_tree.print_tree("inorder"))   
    print("Postorder traversal:", my_tree.print_tree("postorder"))  