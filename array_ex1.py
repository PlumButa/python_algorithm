from array import*

x=array('i',[1,11,22,33,44,55])

print("陣列內容如下:")
for data in x:
    print(data)

i=eval(input("請輸入欲刪除的索引:"))

if i<=5 and i>=0:
    x.pop(i)
    for data in x:
        print(data)
else:
    print("輸入錯誤!")
