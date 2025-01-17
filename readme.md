**first Install necessary modules**<br/>
```pip install pandas uvicorn sqlite3```<br/><br/>
  
**change folder to app directory**<br/>
```
cd app
```<br/><br/>

**run main.py file this will run file server locally**<br/>
```
uvicorn main:app --reload
```<br/><br/>

**to access this running application request on localhost port 8000**<br/>
http://localhost:8000<br/>
http://127.0.0.1:8000<br/><br/>

**Create databse from csv file that is stored in data folder<br/>
there is an API created to do this task<br/>
DO THIS TASK ONLY ONCE(RUN THIS API ONLY ONCE) AS AFTER RUNNING THIS API TWICE IT WILL GIVE ERROR BECAUSE OF DUPLICATE ENTRY IN DATABASE**<br/>
POST http://localhost:8000/createdatabase <br/>
POST http://127.0.0.1:8000/createdatabase<br/><br/>

**To Fetch all budget rules**<br/>
GET http://localhost:8000/allbudgetrules<br/>
GET http://127.0.0.1:8000/allbudgetrules<br/><br/>

**To Fetch all investments**<br/>
GET http://localhost:8000/allinvestments<br/>
GET http://127.0.0.1:8000/allinvestments<br/><br/>

**To Fetch all investments that are passing budget rules**<br/>
GET http://localhost:8000/investmentwithinbudget<br/>
GET http://127.0.0.1:8000/investmentwithinbudget<br/><br/>

**To Fetch all investments that are violating budget rules**<br/>
GET http://localhost:8000/investmentviolatingbudget<br/>
GET http://127.0.0.1:8000/investmentviolatingbudget<br/><br/>


**This is postman Documentation Link Refer incase of seeing output without running code**<br/>
https://documenter.getpostman.com/view/41151004/2sAYQajqn7<br/>
