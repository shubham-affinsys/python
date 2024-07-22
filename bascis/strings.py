from string import Template
st="hello"
print(st[0])
print(st[0:3])

#format strings
print(st+" shubh")
print(f"{st} shubh")
print("%s shubh"%(st))
print("{} shubh".format(st))

st2 = Template("$n1 shubh")
print(st2.substitute(n1=st))

print(st.upper())
print(st.lower())
print(st.isupper())
print(st.islower())

print(st.isalpha())
print(st.isdigit())
print(st.isalnum())
print(st.isascii())
print(st.isdecimal())
print(st.isspace())
print(st.istitle())


print(st.startswith("hel"))
print(st.endswith("lo"))

st3 = ",".join(st)
st4 = "HHH".join(["how","are","you"])

print(st3)
print(st4)


print("my name is shubham".split(" "))
print("how are you".partition("o"))


print(st.rjust(10))  #move 10 spaces to left
print(st.ljust(10))

print(st.rjust(30,"*"))
print(st.ljust(30,"-"))

print(st.center(20,"-"))


print("extraHELLOextraSHUBHextra".strip('extra')) # removes occurce if present in leading and trailling
print("extraHELLOextraSHUBHextra".lstrip('extra')) 
print("extraHELLOextraSHUBHextra".rstrip('extra')) 

#get ascii of a character
print(ord("A"))
# print(ord(st))  will not work on string error
print(chr(65))
print(chr(ord("A")+1))


import pyperclip

pyperclip.copy("hello there")
print(pyperclip.paste())