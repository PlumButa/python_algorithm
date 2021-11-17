class Node():
    def __init__(self, data= None):
        self.data= data         #資料
        self.next= None         #指標

class Linked_list():            #鏈結串列
    def __init__(self):
        self.head= None         #鏈結串列的第1個節點
    
    def print_list(self):       #列印鏈結串列
        ptr= self.head          #指標(ptr)指向第1個鏈結串列
        while ptr:
            print(ptr.data)     #列印節點
            ptr= ptr.next       #移動指標(ptr)到下一個節點
    
    def length(self):
        count= 0
        ptr= self.head
        while ptr:
            count += 1
            ptr= ptr.next
        print("鏈節串列長度是:", count)

link= Linked_list()
link.head= Node(5)
n2= Node(15)
n3= Node(25)
n4= Node(35)

link.head.next= n2
n2.next= n3
n3.next= n4


link.print_list()

link.length()