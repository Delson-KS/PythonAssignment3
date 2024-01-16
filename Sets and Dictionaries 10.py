mylist = list(map(str, input().split()))
myset= set(mylist)
print(myset)
#set already save only unique elements, but if I need to find them in myself
mylist1 = list(map(int, input().split()))
uniquelist= list()
for i in range(len(mylist1)):
    if mylist1[i] not in uniquelist:
        uniquelist.append(mylist1[i])
    else:
        pass
uniqueset=set(uniquelist)
print(uniqueset)
