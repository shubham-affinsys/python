"""
polymorphism :
    one function can have diffrent forms
    same name but different signatures (type and nuo of parameters)
    e.g len() , len("string") , len([10,20,30])

"""

def add(x,y,z=0):
    return x+y+z
print(add(0,20))
print(add(10,20,30))