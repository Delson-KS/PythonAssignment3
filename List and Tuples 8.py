list = list(map(int, input().split()))
max = -999999999
min = 999999999
for i in range(len(list)):
    if(list[i]>max):
        max = list[i]
    if(list[i]<min):
        min = list[i]
print(max,' ',min)

