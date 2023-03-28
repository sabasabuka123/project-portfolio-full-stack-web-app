import pypyodbc as odbc
from flask import Flask, render_template, request
# Set up connection parameters
driver_name = 'SQL Server'
server_name = '192.168.1.4'
database_name = 'test'
uid = 'sa'
pwd = 'SqlPassW0rd'

# Create connection string
connection_string = f'DRIVER={{{driver_name}}};SERVER={server_name};DATABASE={database_name};UID={uid};PWD={pwd}'

# Connect to the database
conn = odbc.connect(connection_string)

# Create cursor object
cursor = conn.cursor()

# Execute a CREATE TABLE statement
# table_name = 'users'
# create_table_query = f"CREATE TABLE {table_name} (id INT IDENTITY(1,1) PRIMARY KEY,  username VARCHAR(50), email VARCHAR(50), password VARCHAR(50))"
# cursor.execute(create_table_query)
#/-----------------------------------------------------------------------------------



# Define query to insert data
# table_name = 'users'
# insert_query = f"INSERT INTO {table_name} (id, name, age) VALUES (?, ?, ?)"

# # Define data to insert
# data = [
#     (1, 'test', 25),
#     (2, 'koba', 30),
#     (3, 'alisa', 35)
# ]

# # Execute the insert query for each row of data
# for row in data:
#     cursor.execute(insert_query, row)


#/---------------------------------------------------------------------------------------
# Define query to add new column
# table_name = 'example_table'
# alter_table_query = f"ALTER TABLE {table_name} ADD address VARCHAR(20)"

# # Execute the alter query
# cursor.execute(alter_table_query)
#------------------------------------------------------------------------------------------

# @app.route('/register', methods=['POST'])
# def register():
#     # Get the user input from the registration form
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']

#     # Insert the user information into the database
#     try:
#         cursor = connection_string.cursor()
#         cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
#         connection_string.commit()
#         return 'Registration successful!'
#     except Exception as e:
#         return f"Error inserting user: {e}"
# ----------------------------------------------------
# Execute the delete statement  just selected row

# cursor.execute("DELETE FROM users WHERE id = ?", (3,))
# --------------------------------
# execute all rows

# cursor.execute("DELETE FROM users ")
# ----------------------------------
# Commit changes to the database
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()