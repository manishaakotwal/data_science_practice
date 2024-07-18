def func():
    print("function")

func()

# arguments
def func(arg):
    print(arg,":argument")

func("a")
func("b")
func("c")

#multiple arguments
def func(fname, lname):
    print(fname, "-" ,lname)

func("manisha","kotwal")

# arbitrary arguments
''' if u do not know how many arg. passed in function as paramenter so u can use * before its name'''
def func(*arg):
    print(arg)

func("arg1", 10 , "arg2")

# keyword arguments - *args
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 

# default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

# passing a list as an argument''
def func(list):
   for i in list:
      print(i)

list=["a", 10,"list_arg"]
func(list)

#return value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))