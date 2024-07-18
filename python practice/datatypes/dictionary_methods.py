# # dictionary methods
# # clear()
# #copy()
# # fromkeys()
# #get()

# dict={
#     "name":"ford",
#     "year":2018
# }

# x= dict.copy()  # copy dictionary in a variable
# dict.clear()   # clear dictionary
# print(dict)
# print(x)

# # fromkeys()
# # syntax - dict.fromkeys(keys, value) 
# # key- required , value - optional
# x = ("key1", " key2", "key3")
# y=0
# thisdict = x.fromkeys(x,y)
# print(thisdict)

#get()
# dictionary.get(keyname, value) 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x) 