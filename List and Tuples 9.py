list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for i in range (len(list2)):
    list1.append(list2[i])
print(list1)