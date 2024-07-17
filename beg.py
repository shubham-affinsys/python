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

"""

