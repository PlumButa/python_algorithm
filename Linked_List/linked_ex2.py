class Node():
    def __init__(self, data= None):
        self.data= data
        self.next= None

class Linked_list():
    def __init__(self):
        self.head= Node
    
    def link_print(self):
        ptr= self.head
        while ptr:
            print(ptr.data)
            ptr= ptr.next
    
    def search_link(self, s1, s2, s3):
        self.s1= s1
        self.s2= s2
        self.s3= s3
        
        print("分別列出",s1,",",s2,",",s3,"的出現次數")

        ptr= self.head
        n1= n2= n3= 0

        while ptr:
            if ptr.data== s1:        #ptr指的是"指標位置"，ptr.data指的是"指標位值的數值"
                n1 += 1
            if ptr.data== s2:
                n2 += 1
            if ptr.data== s3:
                n3 += 1
            ptr= ptr.next

        print(s1,"出現",n1,"次")
        print(s2,"出現",n2,"次")
        print(s3,"出現",n3,"次")

    
link= Linked_list()

print("所建的鏈結串列")

link.head= Node(5)
n2= Node(15)
n3= Node(5)

link.head.next= n2
n2.next= n3

link.link_print()

link.search_link(5,15,20)