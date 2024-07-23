import pyinputplus as inp
import time
strng = inp.inputStr(prompt="enter a string ") #allowRegex= or blockr]Regex=
num = inp.inputNum(prompt="enter a num ",min=1,max=100,timeout=5,limit=3)  #blank =true if want to make it optional

choics=["apple","mango","tomato"]
choice = inp.inputChoice(prompt=f"make a choice -> \n{','.join(choics)}:\n",choices=["mango","apple"])
menu = inp.inputMenu(prompt="choose from menu \n",choices=choics)
# date_time = inp.inputDatetime(prompt="enter date",formats=["%m/%d/%Y ","%H:%M:%S"])
yes_no = inp.inputYesNo(prompt="want to proceed further si for yes and n for no \n",yesVal="si",noVal="no")
bol = inp.inputBool(prompt="type true or false ")
eml = inp.inputEmail("enter your email ")
pth = inp.inputFilepath("enter file path ")
pss = inp.inputPassword("enter your password ")

print(strng)
print(num)
print(choice)
print(menu)
# print(date_time)
print(yes_no)
print(bol)
print(eml)
print(pth)
print(pss)