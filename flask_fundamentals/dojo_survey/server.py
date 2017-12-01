from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    u_name = request.form['name']
    u_location = request.form['A']
    u_language = request.form['languages']
    u_comment = request.form['comment']

    print u_name, u_location, u_language, u_comment
    
    return render_template("/process.html", name=u_name, location=u_location, language=u_language, comment=u_comment)

app.run(debug=True)