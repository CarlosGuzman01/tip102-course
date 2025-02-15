'''
Problem 1: Villager Class
A class constructor is a special method or function that is used to create and initialize a new object from a class. Define the class constructor __init__() for a new class Villager that represents characters in the game Animal Crossing. The constructor accepts three required arguments: strings name, species, and catchphrase. The constructor defines four properties for a Villager:

name, a string initialized to the argument name
species, a string initialized to the argument species
catchphrase, a string initialized to the argument catchphrase
furniture, a list initialized to an empty list
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
Example Usage:

apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)
Output:

Apollo
Eagle
pah
[]

#Understand:
we need to use object oriented programming
we need to create an instance of the class we are creating, in this case the villager class
we need to have 4 fields or members for our class.
    -name which is going to be initialized to the argument name
    -species which is going to be initialized to the argument species
    -catchphrase which is going to be initialized to the argument catchphrase
    -furniture is going to be initialized to an empty list

#Match:
we need a list and using oop

#Plan:

create the class Villager
    declare and initialize the 4 members

make an instance (an object) out of that class

print the properties of the object

'''

#implentation

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchprase = catchphrase
        self.furniture = []
    
    def sayHi(self):
        print("Hi my name is " +  self.name)
        

class Person:
    def __init__(self, namee):
        self.namee = namee
    def sayBye(self):
        print("bye")
        
    

apollo = Villager("Apollo", "Eagle", "pah")
print(apollo)
print(apollo.name)
print(apollo.species)
print(apollo.catchprase)
print(apollo.furniture)
apollo.sayHi()
#print(Villager.__init__("Par", "Cat", "meow", "tr"))
print(Villager.__init__(apollo,"par", "Cat", "meow"))
print(apollo.name)
Villager.sayHi(apollo)

student = Person("Mike")

Villager.sayHi(student)







