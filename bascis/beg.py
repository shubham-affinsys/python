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
dict.has_key(key)   if dict has the key


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



#inheritance

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

p = Person("John","Doe")
p.printname()


class Student(Person):
    def __init__(self,fname,lname,graduated):
        # Person.__init__(self,fname,lname) or use super()
        super().__init__(fname,lname)
        self.graduated = graduated
    
    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to class of",self.graduated)
    def __str__(self):
        return super().__str__()+f" of class {self.graduated}"

s = Student("shubh","chauhan",2025)
s.printname()
s.welcome()
print(s)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"Name : {self.name} Age : {self.age}"

class Employee(Person):
    def __init__(self,name,age,id,dept):
        super().__init__(name,age)
        self.id=id
        self.dept=dept
    def display(self):
        print(super().display(),f"id : {self.id} dept : {self.dept}")

class Student(Person):
    def __init__(self,name,age,id,dob):
        super().__init__(name,age)
        self.id=id
        self.dob=dob
    def display(self):
        print(super().display(), f"id : {self.id} DOB : {self.dob}")



e = Employee("shubh",20,101,"SE")
e.display()

s = Student("Amit",20,102,2003)
s.display()


# default values in function parameters

class Student:
    cur_id=0 # it is a class variable so need to be accesses as cls.cur_id

    @classmethod  # then we dont need to pass cls
    def get_id(cls):
        cls.cur_id+=1
        return cls.cur_id
    
    def __init__(self,name="guest"): # guest is default for name if not given
        self.name=name
        self.id = Student.get_id()
    def __str__(self):
        return f"{self.name} {self.id}"
    
s = Student("shubham")
c = Student("Amit")
d = Student()

print(s,c,d)


"""