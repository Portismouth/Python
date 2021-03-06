from flask import Flask, redirect, session, request, render_template
import random
app = Flask(__name__)
app.secret_key = "the password"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'gold' not in session:
        session['gold'] = 0
    if 'gold_log' not in session:
        session['gold_log'] = []
        
    return render_template('index.html', value=session['gold_log'])

@app.route('/process_money', methods=['POST'])
def get_gold():

    if request.form['Building'] == 'farm':
        farm_gold = random.randrange(10, 21)
        session['gold'] += farm_gold
        session['gold_log'].append("you earned "+str(farm_gold)+" farm gold!")
    elif request.form['Building'] == 'cave':
        cave_gold = random.randrange(5, 11)
        session['gold'] += cave_gold
        session['gold_log'].append("you earned "+str(cave_gold)+" cave gold!")
    elif request.form['Building'] == 'house':
        house_gold = random.randrange(2, 6)
        session['gold'] += house_gold
        session['gold_log'].append("you earned "+str(house_gold)+" house gold!")
    elif request.form['Building'] == 'casino':
        casino_gold = random.randrange(-50, 50)
        session['gold'] += casino_gold
        if casino_gold < 0:
            session['gold_log'].append("you lost "+str(casino_gold)+" gold in the casino...")
        else:
            session['gold_log'].append("you won "+str(casino_gold)+" gold in the casino!")

    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()

    return redirect('/')

app.run(debug=True)
