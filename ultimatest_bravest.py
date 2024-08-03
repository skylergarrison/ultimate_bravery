from flask import Flask, request, render_template, redirect, url_for
import ub
from util_func import eval_bool_string, gen_seed

app = Flask(__name__)

roller = ub.Ub()

@app.route('/')
def index():
    return redirect(url_for('set12'))

@app.route('/set12', methods=['GET', 'POST'])
def set12():
    print(request.args)
    ign_cls = request.args.get('unified', 'false')
    low_pop = request.args.get('low_pop', 'false')

    if request.args.get('roll'):
        seed_val = request.args.get('roll')
    else:
        return redirect('set12?roll=' + gen_seed() + '&unified=' + ign_cls + '&low_pop=' + low_pop)

    roller.roll(
            seed = seed_val,
            ignore_class = eval_bool_string(ign_cls),
            exclude_low = eval_bool_string(low_pop)
        )
    return render_template('roll_result.html', result=roller, ignore=ign_cls, low=low_pop)

if __name__ == '__main__':
    app.run()
