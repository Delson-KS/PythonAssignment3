dict = {"city": "Massachusetts" , "country": "United States","university":"MIT:massachusetts institute of technology" , "dream":"be first"}
check = input("key: ")
if check in dict:
    print(dict[check])
else:
    print("Not found")