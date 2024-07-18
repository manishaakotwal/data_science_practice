# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a:a+10
print(x(5))

x= lambda a ,b : a*b
print(x(4,5))

x= lambda a,b,c : a+b+c
print(x(4,5,6,))

#multiplied with ana unknown number
def myfunc(n):
  return lambda a : a * n 

# this function makes the double of the function parameter
def myfunc(n):
   return lambda a : a * n 
mydoubler = myfunc(2)
print(mydoubler(11))

# this function makes the tripler of the function parameter
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# double and triple
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
