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


    if len(request.form['email']) < 1:
        flash("Please enter your email!", 'noemail')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email!", 'val_email')

    if len(request.form['first_name']) < 2:
        flash("Please enter your first name!", 'error')

    if len(request.form['last_name']) < 2:
        flash("Please enter your last name!", 'error')

    if len(request.form['password']) < 1:
        flash("Please enter your password", 'error')
    elif len(request.form['password']) < 8:
        flash("Your password must be at least 8 characters", 'error')

    if len(request.form['conf_pw']) < 1:
        flash("Please confirm your password", 'error')
    elif request.form['password'] != request.form['conf_pw']:
        flash("Your passwords must match!", 'error')

    password = request.form['password']
    salt = binascii.b2a_hex(os.urandom(15))
    hashed_password = md5.new(password + salt).hexdigest()

    # DB query for stored emails
    query = "SELECT * FROM users WHERE email = :email"
    data = {'email': request.form['email']}
    emails = mysql.query_db(query, data)

    if len(emails) > 0:
        flash("User already exists!")
    else: 
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

    return redirect('/')

@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    print request.form['user_name']
    print request.form['user_password']

    if len(request.form['user_name']) < 1:
        flash("Please enter your email!", 'error')
    elif not EMAIL_REGEX.match(request.form['user_name']):
        flash("Please enter a valid email!", 'error')

    if len(request.form['user_password']) < 1:
        flash("Please enter your password", 'error')

    # DB query for stored emails
    query = "SELECT * FROM users WHERE email = :email"
    data = {'email': request.form['user_name']}
    emails = mysql.query_db(query, data)
    
    if len(emails) > 0:
        flash("You need to register!")
    

    return redirect('/')

@app.route('/users')
def render_userpage():

    return render_template('users.html')

app.run(debug=True)
