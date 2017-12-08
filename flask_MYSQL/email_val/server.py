from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
app.secret_key = "derp"

@app.route('/')
def index():

    status = ""
    if 'email_valid' not in session:
        session['email_valid'] = True

    if session['email_valid'] is False:
        status += "not valid"

    return render_template('index.html', alert = status)

@app.route('/process', methods=['POST'])
def check_email():

    session['new_email'] = request.form['email']

    # DB query for stored emails
    query = "SELECT * FROM email WHERE email = :email"
    data = {'email' : request.form['email']}
    emails = mysql.query_db(query, data)
    
    print emails

    if len(emails) == 0:
        query = "INSERT INTO email (email) VALUES (:email)"
        data = {'email': request.form['email']}
        emails = mysql.query_db(query, data)
        return redirect('/success')
    else:
        session['email_valid'] = False

    return redirect('/')
        

@app.route('/success')
def success():

    query = "select email, date_format(created_at, '%c/%d/%Y %r') AS datetime from email"
    email_list = mysql.query_db(query)
    print email_list
    return render_template('success.html', table=email_list)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



app.run(debug=True)
