#dictionary items contains key value pair and it can be changeble but does not duplicate
# dict={ "name":"manisha"}

dict={
    "name":"manisha",
    "tech":"python"
} 

print(dict)
print(dict["name"])

# *********** changeble ********
dict["name"]="mansi"
print(dict["name"])

#************* not dupliate ********
dict2={
    "name":"manisha",
    "tech":"python",
    "tech":"java"
} 
print(dict2)