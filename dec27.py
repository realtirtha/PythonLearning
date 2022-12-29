#dec 28

class Animal:
    name = ""

    def eat(self):
        print("i can eat")

class Dog(Animal):
    def display(self):
        print("my name is: ", self.name)
    
    def eat(self):
        super().eat()
        print("i can dance")
    

huskey = Dog()
huskey.name = "kalu"
huskey.eat()
huskey.display()

'''
class Room:
    length=0
    breadth=0

    def calculate_area(self):
        print("Area of Room = ", self.length * self.breadth)
    
study_room = Room()
study_room.length = 2
study_room.breadth = 3

study_room.calculate_area()
'''
'''
class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def __str__ (self):
        #return f"{self.name}({self.age})"
        return "new  object"
    def myfunc(self):
        print("the given name is ", self.name)

p1 = Person("Tirtha",20)
p2= Person ("tir",21)

print(p1.name)
print(p1.age)
print(p2)
print(p1)
print(p1.myfunc())

'''

'''
list = [10,20,33,46,55]
newlist = []
print("Given list: ",list)
print("Divisible by 5: ")
for n in list:
    if n%5==0:
        print(n)


##ques 4

for num in range(5):
    for i in range(num):
        print(num, end=" ") #print number
    print("\n")

'''