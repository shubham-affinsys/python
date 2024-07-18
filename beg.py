"""
print("hello")

class Car():
    def __init__(self,*args):
        self.speed=args[0]
        self.color=args[1]

audi = Car(200,'red')
bmw = Car(250,'black')

print(audi.color)
print(bmw.speed)


#dictionary

dict={}
dict["0"]="shubh"
dict["1"]="chauhan"

print(dict["0"])
print(dict["1"])

del(dict["1"])
print(dict)

dict.clear()
dict.copy()
dict.get(key,default="None")
dict.items() --> returns tuple of values
dict.keys()  --> return list of keys
dict.update(dict2) --> updates dict with specified key value pairs
dict values  -->  returns list of all values of dict
dict.pop()  --> removes element with specified key
dict.popItem()  --> removes specified key val pair
dict.setdefaults(key,default="None") set key to default value if key is not specified
dict.has_key(key)  returns true if dict has the key


#classes

class Myclass:
    def __init__(self,name,age): 
        self.name=name
        self.age=age
    def __str__(self): #prints the object as string no need to call the fn
        return f"{self.name} {self.age}"

c=Myclass("shubh",20)
# print(c.name,c.age)

print(c) #print the object __str__ used


delete obj property : del c.age
delete obj : del c



"""
#inheritance

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

p = Person("John","Doe")
p.printname()


class Student(Person):
    pass

s = Student("shubh","chauhan")
s.printname() #inherited method