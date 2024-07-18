# set- store multiple items into single variavle
# it can be changeble or not changeble
# note: it can change by its built in methds only
#set ={,  , }

myset1={"manisha" ,10, "kotwal", 50}
myset={"isha" ,1000, "developer", 5250}
print(myset1)

# can't access by index or key
# access by loops or iterate
for i in myset1:
    print(i)

# update the set using add() or update()
myset1.update(myset)
myset1.add(100)
print(myset1)

#********* remove keyword and methods
# item delete by remove( )or discard()
myset1.remove("manisha")
print()

#******** pop function- remove random items *******
x=myset.pop()
print(x)
print(myset)

#********** clear - makes empty set**********
myset.clear()
print(myset)

#******* del keywaord delete's the set
del myset
print(myset)