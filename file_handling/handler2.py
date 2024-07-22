# import shutil,os
# from pathlib import Path

# p = Path.cwd()

# #copy folder
# shutil.copytree("/folder","backup_folder") #copy folder to other

# #move folder
# shutil.move("src","est")

# #delete folder
# os.unlink("path to file")
# os.rmdir("path to dir")

# shutil.rmtree("apth to to dir")

# # safe delete
# shutil.send2trash("file path") 




# import zipfile

# file_ = str(p)+"f.txt"

# ff = zipfile.ZipFile(file_)

# ff.file_size
# ff.compress_size
# ff.close()

# #extract
# ff.extractall()


#autoclose

class AutoClose:
    def __intit__(self,filename):
        self.filename=filename
    def __enter__(self):
        self.f=open(self.filename)
    def __exit__(self,exc_type,exception,traceback):
        self.f.close()

with AutoClose("/my_files/f.txt") as f:
    print(f.read())
