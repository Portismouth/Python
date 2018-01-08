from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import os
import binascii
app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'thewall')
app.secret_key = "derp"

@app.route('/')
def index():

    if 'user_logged_in' in session:
        return redirect('/wall')

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
        validation_error = True
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
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': request.form['email']}
        new_user = mysql.query_db(query, data)
        session['user_logged_in'] = new_user[0]['id']
        session['user_name'] = new_user[0]['first_name']
        return redirect('/wall')
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

    #authenticate password
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            session['user_logged_in'] = user[0]['id']
            session['user_name'] = user[0]['first_name']
            return redirect('/wall')
        else:
            flash("Invalid password!")
    else:
        flash("Invalid email!")

    return redirect('/')

@app.route('/wall')
def render_userpage():

    query = "SELECT CONCAT(first_name, ' ', last_name) AS user_name, date_format(messages.created_at, '%M %D, %Y') AS date, messages.message, messages.id FROM USERS INNER JOIN messages ON messages.user_id = users.id"
    messages = mysql.query_db(query)

    query = "SELECT CONCAT(first_name, ' ', last_name) AS user_name, date_format(comments.created_at, '%M %D, %Y') AS date, comments.comment FROM USERS INNER JOIN comments ON comments.users_id = users.id INNER JOIN messages ON messages.id = comments.messages_id"
    comments = mysql.query_db(query)

    return render_template('wall.html', all_messages=messages, all_comments=comments)

@app.route('/post-message', methods=['POST'])
def get_post():

    validation_error = False

    if len(request.form['message']) < 1:
        validation_error = True
        flash("Please enter a message to post!", 'error')

    if validation_error is True:
        return redirect('/wall')

    query = "INSERT INTO messages (message, user_id) values(:message , :user_id)"
    data = {
        'message': request.form['message'],
        'user_id': session['user_logged_in']
    }
    new_message = mysql.query_db(query, data)

    return redirect('/wall')


@app.route('/post-comment', methods=['POST'])
def get_comment():

    validation_error = False

    if len(request.form['comment']) < 1:
        validation_error = True
        flash("Please enter a comment to post!", 'error')

    if validation_error is True:
        return redirect('/wall')

    query = "INSERT INTO comments (comment, users_id, messages_id) values(:comment , :user_id, :message_id)"
    data = {
        'comment': request.form['comment'],
        'user_id': session['user_logged_in'],
        'message_id' : request.form['message-id']
    }
    new_message = mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/signout')
def signout():
    session.pop('user_logged_in')
    session.pop('user_name')
    return redirect('/')

#for debugging
@app.route('/reset')
def reset():
    
    session.clear()

    return redirect('/')

app.run(debug=True)
