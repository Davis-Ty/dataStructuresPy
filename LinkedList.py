
#building block of a linked list.. a single element in a linked list
class Node:
    #lets you input data (node=Node(12),node1=Node(6)) 
    #lets you connect data (node.next=node1) to make linked list manually
    def __init__(self, data):
        self.data = data
        self.next = None

# data structure
class LinkedList:
    
    #when creating a linked list (list=LinkedList()) it makes the head None
    def __init__(self):
        self.head = None

    # printing out the element in the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # takes in a value and store as new_node(new_node = Node(data)) (list.insert_at_beginning(3-(data of node))) 
    # makes the value the new head of the list by setting its next value to the prev node 
    #updates the head to the new value since it is a the start of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)

        # checks if the linklist had a head
        # if not it sets out new value to the head then returns
        if not self.head:
            self.head = new_node
            return
        #else it gets head node
        current = self.head

        #loops until next node is empty then set value to next node thats at the end
        while current.next:
            current = current.next
        current.next = new_node

    # takes in two values not includig the list
    # (value that you want to set it behind, the valu itself) 
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Deletes the node who value is passed in
    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev_node = None
        while current and current.data != data:
            prev_node = current
            current = current.next
        if current is None:
            return
        prev_node.next = current.next
        current = None

    # tells user if we have node with vale that was passed in
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # Concatenation puts two list as one
    def concatenate(self, second_list):
        current = self.head
        while current.next:
            current = current.next
        current.next = second_list.head

    #chances the order of the nodes
    def reverse_list(self):
        prev_node = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node

if __name__=='__main__':
    # Create a new linked list object
    my_list = LinkedList()
    my_list1 = LinkedList()

    # Insert nodes with integer values
    my_list.insert_at_beginning(5)
    my_list.insert_at_end(10)
    my_list.insert_after(my_list.head, 7)

    my_list1.insert_at_end(4)
    my_list1.insert_at_end(5)
    my_list1.insert_at_end(6)  

    print("print the list")
    my_list.traverse()

    print("reverse list")
    my_list.reverse_list()
    my_list.traverse()

    print("print the 2 list")   
    my_list1.traverse()


    #putting list and list1 as list1
    print("list combine")
    my_list.concatenate(my_list1)
    my_list.traverse()
    

    #head is what the first node is
    print("head")
    #use .data to get the value itself and not the address
    print(my_list.head.data)

    print("Do we have a node with value 3")
    print(my_list.search_node(3))
    print("Do we have a node with value 10")
    print(my_list.search_node(10))
    
    print("delete 10")
    my_list.delete_node(10)

    print("Do we have a node with value 10")
    print(my_list.search_node(10))