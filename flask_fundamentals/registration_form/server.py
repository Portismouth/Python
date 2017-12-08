from flask import Flask, request, redirect, render_template, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "poop"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    
    if len(request.form['email']) < 1:
        flash("Please enter your email!", 'noemail')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email!", 'val_email')

    if len(request.form['first_name']) < 1:
        flash("Please enter your first name!", 'error')
    if len(request.form['last_name']) < 1:
        flash("Please enter your last name!", 'error')
    if len(request.form['password']) < 1:
        flash("Please enter your password", 'error')
    if len(request.form['conf_password']) < 1:
        flash("Please confirm your password", 'error')
    elif request.form['password'] != request.form['conf_password']:
        flash("Your passwords must match!", 'error')

    return redirect('/')

app.run(debug=True)
