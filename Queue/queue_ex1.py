class Queue():
    def __init__(self):
        self.queue= []
    
    def enqueue(self, data):
        self.queue.insert(0,data)
        print("成功插入",data,"至佇列")
    
    def size(self):
        print("佇列長度是:",len(self.queue))

q= Queue()

for i in ["漢堡","薯條","可樂","雞塊"]:
    q.enqueue(i)

q.size()
