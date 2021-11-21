from queue import Empty, Queue

q= Queue()

for i in ["漢堡","薯條","可樂","雞塊"]:
    q.put(i)
    print("成功插入",i,"至佇列")

print("佇列輸出")

while q.empty() == False:
    print(q.get())
