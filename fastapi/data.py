employee=[
    {
        "id":1,
        "name":"root",
        "age":0,
        "gender":"male",
        "team":"admin"
    },
    {
        "id":2,
        "name":"shubh",
        "age":20,
        "gender":"male",
        "team":"Implementation"
    }
]

def get_emp_data(emp_id):
    for emp in employee:
        if emp["id"]==emp_id:
            return emp
    return "employee does not exist"

def get_all_emps():
    return employee