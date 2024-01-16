list = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# 0,1,2,3,4,5,6,7,8,9
index = len(list)//2-2
list1=[]
count=0
for i in range(5):
    list1.append(list[index+i])
print(list1)