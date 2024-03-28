from flask import Flask, request, render_template, redirect
import ub
import random

app = Flask(__name__)

roller = ub.Ub()

@app.route('/')
def index():
    seed = str(random.randint(1, 8783818952879679611000))
    print('Seed is: ' + seed)

    return redirect('/set11?roll=' + seed)

@app.route('/set11', methods=['GET', 'POST'])
def set11():
    if request.args:
        roller.roll(request.args.get('roll'))
        return render_template('roll_result.html', result=roller)
        
    else:
        return index()

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
