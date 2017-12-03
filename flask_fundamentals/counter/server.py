from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def index():
    session['counter'] += 1

    return render_template("index.html")

@app.route('/addtwo', methods=['POST'])
def add_two():
    session['counter'] += 1

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    
    return redirect('/')

app.run(debug=True)
