from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
import data

#deployed on https://acc-balance.vercel.app/
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory data store


# Parsing XML data
users_data = fromstring(data.users_xml)
cif_to_uer_id_data = fromstring(data.cif_to_user_id_xml)
phone_to_user_id_data = fromstring(data.phone_to_user_id_xml)
account_to_user_id_data = fromstring(data.account_to_user_id_xml)

class Account(BaseModel):
    balance: float

@app.get("/")
def get_home():
    return "Your are at the Bank"

@app.get("/accounts")
def get_all_accounts():
    # return accounts
    all_accs = []
    for usr in data.accounts:
        ussr = data.accounts[usr]
        all_accs.append(ussr["accounts"])
    return all_accs

@app.get("/users")
def get_all_users():
    # return accounts
    all_users = []
    for usr in users_data:
        all_users.append(usr)
    return all_users


@app.get("/users/{user_id}")
def get_user(user_id:str):
    if user_id in users_data.keys():    
        return users_data[user_id]
    raise HTTPException(status_code=404,detail="user not found")

# @app.get("/accounts/{account_number}")
# def get_balance(account_number: str):
#     for account in accounts:
#         if account["account_number"] == account_number:
#             return {"account_number": account_number, "balance": account["balance"]}
#     raise HTTPException(status_code=404, detail="Account not found")

# # create new account not using it
# @app.post("/accounts/{account_number}")
# def create_account(account_number: str, account: Account):
#     if any(acc["account_number"] == account_number for acc in accounts):
#         raise HTTPException(status_code=400, detail="Account already exists")
#     new_account = {
#         "title": f"101xxxx{account_number[-4:]}",
#         "account_no": account_number,  
#         "balance": account.balance,
#         "payload": account_number,
#         "type": "payload"
#     }
#     accounts.append(new_account)
#     return {"message": "Account created", "account_number": account_number, "balance": account.balance}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)