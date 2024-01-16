list = [9,7,2,1,3]
num = int(input())
if num in list:
    for i in range(len(list)):
        if list[i] == num:
            index=i
    print("Number in list, index is ", index)
