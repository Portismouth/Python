from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import os
import binascii
app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'login_registration')
app.secret_key = "derp"

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    validation_error = False

    if len(request.form['email']) < 1:
        validation_error = True
        flash("Please enter your email!", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        validation_error = True
        flash("Please enter a valid email!", 'error')
        
    if len(request.form['first_name']) < 2:
        validation_error = True
        flash("Please enter your first name!", 'error')

    if len(request.form['last_name']) < 2:
        validation_error = True
        flash("Please enter your last name!", 'error')

    if len(request.form['password']) < 1:
        validation_error = True
        flash("Please enter your password", 'error')
    elif len(request.form['password']) < 8:
        vaildation_error = True
        flash("Your password must be at least 8 characters", 'error')

    if len(request.form['conf_pw']) < 1:
        validation_error = True
        flash("Please confirm your password", 'error')
    elif request.form['password'] != request.form['conf_pw']:
        validation_error = True
        flash("Your passwords must match!", 'error')

    if validation_error is True:
        return redirect('/')

    password = request.form['password']
    salt = binascii.b2a_hex(os.urandom(15))
    hashed_password = md5.new(password + salt).hexdigest()

    # DB query for stored emails
    query = "SELECT * FROM users WHERE email = :email"
    data = {'email': request.form['email']}
    emails = mysql.query_db(query, data)

    if emails == []:
        query = "INSERT INTO users (first_name, last_name, email, password, salt) VALUES(:first_name, :last_name, :email, :password, :salt)"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password' : hashed_password,
            'salt' : salt
        }
        usersdb = mysql.query_db(query, data)
        return redirect('/users')
    else:
        flash("User already exists!") 

    return redirect('/')

@app.route('/authenticate', methods=['POST'])
def authenticate_user():

    validation_error = False

    if len(request.form['user_name']) < 1:
        validation_error = True
        flash("Please enter your email!", 'error')
    elif not EMAIL_REGEX.match(request.form['user_name']):
        validation_error = True
        flash("Please enter a valid email!", 'error')

    if len(request.form['user_password']) < 1:
        validation_error = True
        flash("Please enter your password", 'error')

    if 'user_logged_in' in session:
        validation_error = True
        flash('You are already logged in')

    if validation_error is True:
        return redirect('/')

    email = request.form['user_name']
    password = request.form['user_password']

    # DB query for stored emails
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    print user

    #authenticate password
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            session['user_logged_in'] = user[0]['id']
            session['user_name'] = user[0]['first_name']
            print session['user_name']
            return redirect('/users')
        else:
            flash("Invalid password!")
    else:
        flash("Invalid email!")

    return redirect('/')

@app.route('/users')
def render_userpage():

    return render_template('users.html')

@app.route('/reset')
def reset():
    
    session.clear()

    return redirect('/')

app.run(debug=True)
