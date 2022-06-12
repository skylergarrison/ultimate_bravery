from flask import Flask, render_template
import ub

app = Flask(__name__)

roller = ub.Ub()

@app.route("/")
def display_roll():
    roller.roll()
    return render_template('roll_result.html', result=roller)
