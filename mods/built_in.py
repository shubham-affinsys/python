"""
import os
print(os.getcwd())
dirs = os.listdir()
print(dirs)


import random
print(random.randint(1,100))
print(random.choice([10,20,40,30]))

import sys

#take input from console while runing python file in cmd
# print("My name is{}. I am {} years old".format(sys.argv[1],sys.argv[2]))
print(sys.path)
print(sys.version)

import collections

#named tuples
employee = collections.namedtuple("employee",["name","age","salary"])
e1 = employee("shubham",21,100)
print(e1.name,e1.age,e1.salary)

#Ordered dictionary  order of insertion
d = collections.OrderedDict()
d['a']=10
d['b']=20
d['c']=50
d['d']=40

for k,v in d.items():
    print(k,v)


#deque
q = collections.deque([10,20,30,40])
q.append(120)
print(q)

q.pop()
print(q)

q.popleft()
print(q)

#statistic modules

import statistics

mean  = statistics.mean([2,5,10,18])
print(mean)

meadian = statistics.median([1,10,2,4,18])
print(meadian)

mode = statistics.mode([1,20,3,4,50])
print(mode)

standard_deviation = statistics.stdev([1,10,2.5,8,9,7])
print(standard_deviation)

#time
import time
t = time.time()
print(t)

print(time.localtime())
print(time.asctime())
print(time.ctime())





#file io

character	purpose
r	Opens a file for reading only. (default)
w	Opens a file for writing only, deleting earlier contents
a	Opens a file for appending.
t	opens file in text format (default)
b	Opens a file in binary format.
+	Opens a file for simultaneous reading and writing.
x	opens file for exclusive creation.



f = open("input.txt","rb")
print(f.readlines())
f.close()

f = open("input.txt","wb")
f.write(int.to_bytes(1024,16,"big"))
print(f.closed)
print(f.mode)
print(f.name)


"""

#csv
import csv

#crete and write in csv
marks = [('shubh',20,100),('Abh',29,70),('mike',92,2)]
csvfile = open('marks.csv','w',newline='')
obj = csv.writer(csvfile)
for row in marks:
    obj.writerow(row)
csvfile.close()


#read from csv
csvfile = open('marks.csv','r',newline='')
obj = csv.reader(csvfile)
for row in obj:
    print(row)

while True:
    try:
        row=next(obj)
        print(row)
    except StopIteration:
        break


