from flask import Flask
import ub

app = Flask(__name__)

roller = ub.Ub()

@app.route("/")
def display_roll():
    roller.roll()
    return f'<p><strong>Synergies:</strong> {roller.roll_result}</p><p><strong>Royal:</strong> {roller.royal}</p><p><strong>Champions:</strong> {roller.legal_champs}</p>'