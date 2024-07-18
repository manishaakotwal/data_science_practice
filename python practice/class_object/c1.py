'''class myclass:
    x=4
    print("class declare")

p1 = myclass()   # p1 object declare
print(p1.x)'''

# __init__() - executed when the class is being initiated. & assign value & operation
class person:
    def __init__(self, name, gender, profession):
        self.name= name
        self.gender= gender
        self.profession= profession
    
    def show_details(self):
        print("name:",self.name ,"gender:",self.gender, "profession:", self.profession)

    def show_work(self):
        print(self.name, "working as a" ,self.profession)

john = person("jessa","female","software engginear")
john.show_details()
john.show_work()            
        


