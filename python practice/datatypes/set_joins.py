# union - method returns a new set with all data types
set1={1,'a',4,"union"}
set2={3,'b', 5,'c'}
set3=set1.union(set2)
print(set3)


set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)

# using another method | 
myset1= set1 | set2| set3 | set4
print(myset) 
print(myset1) 

# update - update set items one into another
set1 = {'a','b','c'}
set2= {1,2,3}
set1.update(set2)
print(set1)

# intersection using - dot(.) or &
# intersection - keeps only the duplicates
set1 = {'a','b','c'}
set2= {'a',2,'c'}
set3=set1.intersection(set2)
set4= set1 & set2
print(set3)
print(set4)

'''The intersection_update() method will also keep ONLY the duplicates, 
but it will change the original set instead of returning a new set.'''
set1.intersection_update(set2)
print(set1) 

# difference
''' The difference() method will return a new set that will contain only the items from 
the first set that are not present in the other set.
'''
set1 = {'a','b','c'}
set2= {'a',2,'c'}
set5=set1.difference(set2)
set3= set1 - set2
print(set5)
print(set3)

# difference_update
set1.difference_update(set2)
print(set1)

#symmetric difference
#The symmetric_difference() method will keep only the elements
#  that are NOT present in both sets.
set1 = {'a','b','c'}
set2= {'a',2,'c'}
set5=set1.symmetric_difference(set2)
print(set5)
