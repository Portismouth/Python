from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "camel teet"



@app.route('/')
def index():
    rand_num = random.randrange(1, 101)
    if 'number' not in session:
        session['number'] = rand_num
        
    if 'guess' not in session:
        session['guess'] = 0

    print session['number']

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def get_guess():
    session['guess'] = int(request.form['guess'])

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()

    return redirect('/')


app.run(debug=True)
