from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from data import employee,get_emp_data, get_all_emps
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class emp(BaseModel):
    name:str
    age:int
    team : Union[str,None] = None 

@app.get("/")
def read_root():
    return "go to /emps/{emp_id} to get data about the employee"

@app.get("/emps")
def read_root():
    try:
        all_emps = get_all_emps()
        return all_emps
    except Exception as e:
        print("error occured")
        return {"error :":str(e)}


@app.get("/emps/{emp_id}")
def read_data(emp_id:int):
    try:
        emp_data = get_emp_data(emp_id)
        return emp_data
    except Exception as e:
        return {"error: ":str(e)}

@app.put("/emps/{emp_id}")
def update_emp(emp_id:int,emp:emp):
    #update employee data in db
    return {"emp_name:":emp.name,"emp_age: ":emp.age,"emp_team":emp.team}

@app.post("/emps/{emp_id}")
def new_emp(emp_id:int,emp:emp):
    # add employee to db
    return "new employee added"