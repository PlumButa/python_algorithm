from array import*

x=array('i',[1,11,22,33,44,55])

print("陣列內容如下:")
for data in x:
    print(data)

i=eval(input("請輸入欲插入的索引:"))
j=eval(input("請輸入欲插入的數值:"))

if i<=5 and i>=0:
    x.insert(i,j)
    for data in x:
        print(data)
else:
    print("輸入錯誤!")
