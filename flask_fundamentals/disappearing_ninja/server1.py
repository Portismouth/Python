from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def show_ninja(color):
    return render_template("ninjas.html", color=color)


app.run(debug=True)
