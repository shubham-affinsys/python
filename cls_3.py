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