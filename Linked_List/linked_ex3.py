class Node():
    def __init__(self, data= None):
        self.data= data
        self.next= None
        self.previous= None
    
class Linked_list():
    def __init__(self):
        self.head= None
        self.tail= None
    
    def print_next_link(self):
        print("從頭部列印雙向鏈結串列")
        ptr= self.head
        while ptr:
            print(ptr.data)
            ptr= ptr.next
    
    def print_previous_link(self):
        print("從尾部列印雙向鏈結串列")
        ptr= self.tail
        while ptr:
            print(ptr.data)
            ptr= ptr.previous

    def add_double_list(self, new_node):
        if isinstance(new_node, Node):
            if self.head== None:
                self.head= new_node
                new_node.next= None
                new_node.previous= None
                self.tail= new_node
            else:
                self.tail.next= new_node
                new_node.previous= self.tail
                self.tail= new_node


link= Linked_list()

for data in ["Sun","Mon","Thu","Web","Tue","Fri","Sat"]:
    link.add_double_list(Node(data))

# link.add_double_list(Node("Sun"))
# link.add_double_list(Node("Mon"))
# link.add_double_list(Node("Thu"))
# link.add_double_list(Node("Web"))
# link.add_double_list(Node("Tue"))
# link.add_double_list(Node("Fri"))
# link.add_double_list(Node("Sat"))

link.print_next_link()
link.print_previous_link()