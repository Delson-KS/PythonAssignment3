dict1 = {"city": "Massachusetts" , "country": "United States","university":"MIT:massachusetts institute of technology" , "dream":"be first"}
dict2 = {"name":"Kaiyrekeldi" , "surname":"Sagitzhan","graduated":"AITU:Astana IT university"}
dict2.update(dict1)
for key, value in dict2.items():
    print(key,":", value)