from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "boob"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():

    error_exists = False

    u_name = request.form['name']
    u_location = request.form['A']
    u_language = request.form['languages']
    u_comment = request.form['comment']

    if len(u_name) < 1:
        error_exists = True
        flash("Name cannot be empty!")
    
    if len(u_comment) < 1 or len(u_comment) > 120:
        error_exists = True
        flash("Something about the comment")

    if error_exists == True:
        return redirect('/')
    
    return render_template("process.html", name=u_name, location=u_location, language=u_language, comment=u_comment)

app.run(debug=True)
