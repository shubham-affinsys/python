from pathlib import Path

p = Path("python","file_handler","handler.py")
print(p)

myfiles = ["beg.py","iss.txt","strings.py"]

for files in myfiles:
    print(Path(Path.cwd(),files))

import os
os.chdir("/home/shubham/work/webd")

print(Path.cwd())

os.chdir(Path.home())
print(Path.cwd())

# os.makedirs(Path("/home/shubham/work/python/file_handling/"+"my_files"))

print(Path.cwd().is_absolute()) #check if path is absolute

relative_path = "work/webd"
get_abs_apth = str(Path.cwd())+"/"+relative_path
print(Path(get_abs_apth))

os.chdir(get_abs_apth)

p = Path("handler.py")
print(p.name)
print(p.drive)
print(p.stem)
print(p.suffix)
print(str(p.parent))
print(p.anchor)

print(os.path.dirname("handle.py"))

pt = Path.cwd()
print(list(pt.glob("*")))

os.chdir("/home/shubham/work/python/file_handling")
pt2 = Path(str(Path.cwd())+"/my_files/f.txt")
pt2.write_text("hello")

print(pt2.read_text())

f = open(pt2,"r+")
f.readlines()

f.write(" new line")
f.close

import shelve
mysheleve = shelve.opne("my_stored_data_file")
new_setting = ["item2","resource3"]

mysheleve["settings"]=new_setting

mysheleve.close()