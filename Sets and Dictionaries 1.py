fromUser = list(map(int, input().split()))
nums = {''}
for i in range(len(fromUser)):
    nums.add(fromUser[i])
nums.discard('')
print(nums)
