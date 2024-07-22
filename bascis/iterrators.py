"""
Iterators :
    object that contains number of values
    can be ierated upon (tarverse)
    object which implements iterator protocol
    which consist of methods __iter__() and __next__()
"""

string = "Shubham"
ch_iterator = iter(string)
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))

########################
#self defined iterator

class Test:
    def __init__(self,limit):
        self.limit=limit
    
    def __iter__(self):
        self.x=10
        return self
    
    def __next__(self):
        x=self.x
        if x>self.limit:
            raise StopIteration
        self.x +=1
        return x

#Prints numbers from 10 to 15
for i in Test(15):
    print(i)
#prints nothing
for i in Test(5):
    print(i)



########################

#iterate over an built in iterator (list,tuple,dict)

print("List iteration")
ls = ["shubh","amit","vijayant"]
for i in ls:
    print(i)

print("\nTuple iteration")
tl = ("shubh","amit","vijyant")
for i in tl:
    print(i)

print("\nString iteration")
st = "shubh"
for i in st:
    print(i)

print("\nDictionary iteration")
d = dict()
d["abc"] = 123
d["xyz"] = 567
for i in d:
    print("%s %d"%(i,d[i]))


#################
#iterating inside iterator

tup = ("shubh","was","here","you","are","where")

tup_iter = iter(tup)
print("inside loop: ")

for idx,item in enumerate(tup_iter):
    print(f"idx  : {idx} item : {item}")
    if idx==2:
        break

print("outside loop")
print(next(tup_iter))
print(next(tup_iter))


