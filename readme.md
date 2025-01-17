<!-- first Install necessary modules -->
pip install pandas uvicorn sqlite3

<!-- change folder to app directory -->
cd app

<!-- run main.py file this will run file server locally -->
uvicorn main:app --reload

<!-- to access this running application request on localhost port 8000 -->
http://localhost:8000
http://127.0.0.1:8000

<!-- Create databse from csv file that is stored in data folder -->
<!-- there is an API created to do this task -->
<!-- DO THIS TASK ONLY ONCE(RUN THIS API ONLY ONCE) AS AFTER RUNNING THIS API TWICE IT WILL GIVE ERROR BECAUSE OF DUPLICATE ENTRY IN DATABASE -->
POST http://localhost:8000/createdatabase 
POST http://127.0.0.1:8000/createdatabase

<!-- To Fetch all budget rules -->
GET http://localhost:8000/allbudgetrules
GET http://127.0.0.1:8000/allbudgetrules

<!-- To Fetch all investments -->
GET http://localhost:8000/allinvestments
GET http://127.0.0.1:8000/allinvestments

<!-- To Fetch all investments that are passing budget rules -->
GET http://localhost:8000/investmentwithinbudget
GET http://127.0.0.1:8000/investmentwithinbudget

<!-- To Fetch all investments that are violating budget rules -->
GET http://localhost:8000/investmentviolatingbudget
GET http://127.0.0.1:8000/investmentviolatingbudget


<!-- This is postman Documentation Link Refer incase of seeing output without running code -->
https://documenter.getpostman.com/view/41151004/2sAYQajqn7