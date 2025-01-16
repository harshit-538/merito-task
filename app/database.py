# database in connected and stored/populated..
import pandas as pd
import sqlite3

db_name = "merito.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

#############################################################
#adding budget table in database
budget = pd.read_csv('budget.csv')
budget = budget.mask(budget == '')
table_name = "budget"

#CREATE TABLE 
# columns = ", ".join([f"{col} TEXT" for col in budget.columns])  # Assuming all columns are TEXT
# create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
# cursor.execute(create_table_query)

# #POPULATE TABLE
# for _, row in budget.iterrows():
#     placeholders = ", ".join(["?" for _ in row])  # Placeholders for parameterized query
#     insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
#     cursor.execute(insert_query, tuple(row))

#PRINT TABLE
# print_query = f"SELECT * FROM {table_name}"
# cursor.execute(print_query)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

########################################################
investment = pd.read_csv('investments.csv')
investment = investment.mask(investment=='')
table_name2 ="investment"

#CREATE TABLE 
# columns = ", ".join([f"{col} TEXT" for col in investment.columns])  # Assuming all columns are TEXT
# create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name2} ({columns});"
# cursor.execute(create_table_query)

# #POPULATE TABLE
# for _, row in investment.iterrows():
#     placeholders = ", ".join(["?" for _ in row])  # Placeholders for parameterized query
#     insert_query = f"INSERT INTO {table_name2} VALUES ({placeholders});"
#     cursor.execute(insert_query, tuple(row))

#PRINT TABLE
# print_query = f"SELECT * FROM {table_name2}"
# cursor.execute(print_query)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


conn.commit()
conn.close()

# print(f"Data from budget successfully inserted into {db_name} in table {table_name}.")
