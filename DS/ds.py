#dictionary
mydog = {"size":10,"color":"orange","age":3}

print(mydog["size"])

for att in mydog:
    print(att,mydog[att])

mypets = [
    {
        "cat":"tom",
        "size":20,
        "color":"white"
    },
    {
        "dog":"doggy",
        "size":50,
        "color":"brown",
        "age":5,
        "breed":"German shephard"
    }
]

for pet in mypets:
    for att in pet:
        print(att,pet[att])

#or 
for pet in mypets:
    for key in pet:
        print(key,pet[key])

print(mydog == mypets)

print(mydog.keys()) # return list of keys
print(mydog.values()) # print list of values

print("size" in mydog.keys())
print("orange" in mydog.values())

items = {"apple":10,"orange":9}

apple = items.get("apple",0)  # return 0 if apple does not exist in list
mango = items.get("mango",0)

print(f"apples: {apple}, mango: {mango}")

if "mango" not in items:
    items["mango"]=1

apple = items.get("apple",0)
mango = items.get("mango",0)

print(f"apples: {apple}, mango: {mango}")

banana = items.get('banana',0)
print(banana)

items.setdefault("banana",4)
banana = items.get('banana',0)
print(banana)

items.setdefault("banana",8) # value will not be updated
banana = items.get('banana',0)
print(banana)

import pprint #prety print
pprint.pprint(mypets)

print(pprint.pformat(mypets))