# # # list
# # mylist = ["apple", "mango", "cherry"]
# # #list are ordered , changeble and allow duplicate
# # print(mylist)
# # mylist[0]="orange"
# # print(mylist)
# # mylist.append("strawberry")
# # print(mylist)

# # # append= items add
# # #extend = iterable
# # # two list add
# # l1= [1,"mani", 3,"kotwal"]
# # l2= [4, "together",6, "everyone","achives"]
# # l1.extend(l2)
# # print(l1)

# # change 
# l1= ["apple", "orange","cherry"]
# l1[1:3]= ["watermelon"]
# print(l1)

# #add list itmens
# l2= ["apple", "orange","cherry"]
# l2.insert(1,"aalooo")
# print(l2)

# #remove list items
# l1 =['a','b','c']
# l2= ['d','e','f']
# l1.remove('b')
# print(l1)
# l1.pop()
# print(l1)
# l1.pop(2)
# print(l1)

# l =[1,2,3,4,4,5]
# dic= {}
# for i in l:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)

l =[1,2,3,4,4,5]
dic= {}
# count=0
# for i in l:
#     if i in l:
#         count+=1
#         dic[i]=count
#     else:
#          dic[i]=count 
# print(dic)    
for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

ch = "manishakotwal "
d ={}
for i in ch:
    if i in d:
        d[i] += 1
    else:
        d[i]= 1
print(d)   

l1 = [1,2,4,5]
l2 = [6,5,7,1]
r_list = []
for i in range(0,len(l1)):
    r_list.append(l1[i]*l2[i])

print(r_list)

