from flask import Flask, request, render_template
import ub

app = Flask(__name__)

roller = ub.Ub()

@app.route('/')
def index():
    roller.roll()
    return render_template('roll_result.html', result=roller)

@app.route('/set10', methods=['GET', 'POST'])
def set10():
    roller.roll()
    return render_template('roll_result.html', result=roller)

@app.route('/set3', methods=['GET', 'POST'])
def set3():
    roller.roll(3)
    return render_template('roll_result.html', result=roller)

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
