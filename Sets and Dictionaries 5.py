frequency={}
fromuser = input()
for char in fromuser:
    frequency[char]=frequency.get(char,0) + 1
result =frequency
for char,frequency in frequency.items():
    print(char,frequency)