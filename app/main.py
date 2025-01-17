from fastapi import FastAPI,APIRouter,HTTPException
import sqlite3
import pandas as pd

app = FastAPI()
router = APIRouter()

DB_FILE = "merito.db"

# Utility function to execute database queries
def execute_query(query, params=(), fetch_all=True):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch_all:
            return cursor.fetchall()
        conn.commit()

@app.get("/")
def root():
    return {'message':'home Page'}

@app.post("/createdatabase")
def CreateDB():

    #####################################################
    ##Create Budget database
    budget = pd.read_csv('data/budget.csv')
    budget = budget.mask(budget == '')
    table_name = "budget"

    #CREATE TABLE 
    create_table_query = f'''CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGET PRIMARY KEY,
            Amount INTEGET,
            Time_Period TEXT,
            SECTOR TEXT);'''
    execute_query(create_table_query)

    #POPULATE TABLE
    for _, row in budget.iterrows():
        placeholders = ", ".join(["?" for _ in row])  # Placeholders for parameterized query
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
        execute_query(insert_query, tuple(row))

    ################################################
    ###Create Investments Database...
    investment = pd.read_csv('data/investments.csv')
    investment = investment.mask(investment=='')
    table_name2 ="investment"

    #CREATE TABLE 
    create_table_query = f'''CREATE TABLE IF NOT EXISTS {table_name2} (
            id INTEGET PRIMARY KEY,
            Date TEXT,
            Amount INTEGER,
            SECTOR TEXT);'''
    execute_query(create_table_query)

    #POPULATE TABLE
    for _, row in investment.iterrows():
        placeholders = ", ".join(["?" for _ in row])  # Placeholders for parameterized query
        insert_query = f"INSERT INTO {table_name2} VALUES ({placeholders});"
        execute_query(insert_query, tuple(row))
    
    return {"message":"Database Created Successfully"}


@app.get("/allbudgetrules")
def getAllBudget():
    query = 'SELECT * FROM budget'
    records = execute_query(query)
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return {"data": records}

@app.get("/allinvestments")
def getAllInvestment():
    query = 'SELECT * FROM investment'
    records = execute_query(query)
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return {"data": records}

@app.get("/investmentwithinbudget")
def InvestmentWithinBudget():
    investment_data,result_list = Manage()
    # print(investment_data)
    # print(result_list)

    investment_in_budget = []
    for row,result in zip(investment_data,result_list):
        if(result):
            investment_in_budget.append(row)

    return {'data':investment_in_budget}

@app.get("/investmentviolatingbudget")
def InvestmentViolatingBudget():
    investment_data,result_list = Manage()

    investment_in_budget = []
    for row,result in zip(investment_data,result_list):
        if(not result):
            investment_in_budget.append(row)

    return {'data':investment_in_budget}

def Manage():
    query = "SELECT * FROM budget"
    budget_data = execute_query(query)

    ds = {}

    for row in budget_data:
        if(row[3]):
            if(row[2] == 'Month'):
                ds[row[3]] = [int(row[1])] * 12
            elif(row[2] == 'Quarter'):
                ds[row[3]] = [int(row[1])] * 4
            else:
                ds[row[3]] = [int(row[1])]
        else:
            if(row[2] == 'Month'):
                ds[f"Other {row[2]}"] = [int(row[1])] * 12
            elif(row[2] == 'Quarter'):
                ds[f"Other {row[2]}"] = [int(row[1])] * 4
            else:
                ds["Other"] = [int(row[1])]
    
    # print(ds)
    
    query1 = "SELECT * FROM investment"
    investment_data = execute_query(query1)

    result_list = []

    for row in investment_data:
        result = True
        set = ["BigData","E-Commerce","FinTech"]
        sector = row[3] if (row[3] in set) else "Other"
        date = row[1]
        month = int(date.split("/")[1])
        amount = int(row[2])

        if(ds['Other Month']):
            Monthly_list = ds['Other Month']

        Yearly_budget = ds['Other'][0]

        if(sector!="Other"):
            budget_list = ds[sector]
            if(len(budget_list) == 1):
                if(Yearly_budget>=amount and Monthly_list[month-1] >= amount and amount <= ds[sector][0]):
                    ds[sector][0] -= amount
                    Monthly_list[month-1] -=  amount
                    Yearly_budget -= amount
                else:
                    result = False
            elif(len(budget_list) == 4):
                quat = (month-1)//3
                if(Yearly_budget>=amount and Monthly_list[month-1] >= amount and amount <= ds[sector][quat]):
                    ds[sector][quat] -= amount
                    Monthly_list[month-1] -=  amount
                    Yearly_budget -= amount
                else:
                    result = False
            else: 
                if(Yearly_budget>=amount and Monthly_list[month-1] >= amount and amount <= ds[sector][month-1]):
                    ds[sector][month-1] -= amount
                    Monthly_list[month-1] -=  amount
                    Yearly_budget -= amount
                else:
                    result = False
        else:
            if(Yearly_budget>=amount and Monthly_list[month-1] >= amount):
                    Monthly_list[month-1] -=  amount
                    Yearly_budget -= amount
            else:
                result = False

        result_list.append(result)

    return investment_data,result_list