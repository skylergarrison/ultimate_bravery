from flask import Flask, render_template
import ub
import os

THUMBNAIL_PATH = os.path.join('static', 'champ_thumbs')

app = Flask(__name__)
app.config['THUMBNAIL_FOLDER'] = THUMBNAIL_PATH

roller = ub.Ub()

@app.route("/")
def display_roll():
    roller.roll()
    full_filename = os.path.join(app.config['THUMBNAIL_FOLDER'], 'aatrox.png')
    return render_template('roll_result.html', result=roller, photo=full_filename)
