from flask import Flask, render_template,request
import pyodbc
import yagmail


app = Flask(__name__)
server = '192.168.1.4'
database = 'test'
username = 'sa'
password = 'SqlPassW0rd'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
@app.route("/")
def hello_world():
    return render_template('home.html')
@app.route("/result",methods=['POST',"GET"])
def register():
    output = request.form.to_dict()
    # Get the user input from the registration form
    username = output['username']
    email = output['email']
    password = output['password']
    
    # Insert the user information into the database
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    cnxn.commit()
    # Select all emails from the users table
    cursor = cnxn.cursor()
    cursor.execute('SELECT TOP 1 email FROM users ORDER BY id DESC')
    result = cursor.fetchone()
    if result:
        last_email = result.email
        print('Last inserted email:', last_email)
        # Create the email message
        sender='dummbadzesabaa@gmail.com'
        reciver=last_email
        subject='registraciaaa'
        content = '''hello, you register succesfully. '''
        
        yag=yagmail.SMTP(user=sender,password='tsivrgxjuiqspvof')
        yag.send(to=reciver,subject=subject,contents=content)
        print('email.sent')
    else:
        print('No emails found in the registration table')
    
    
    # Return a success message to the user
    return 'Registration successful!'
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)