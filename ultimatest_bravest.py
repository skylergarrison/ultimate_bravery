from flask import Flask, request, render_template, redirect, url_for
import ub
from util_func import eval_bool_string, gen_seed

app = Flask(__name__)

roller = ub.Ub()

@app.route('/')
def index():
    return redirect(url_for('bravery'))

@app.route('/bravery', methods=['GET', 'POST'])
def bravery():
    print(request.args)
    ign_cls = request.args.get('unified', 'false')
    low_pop = request.args.get('low_pop', 'false')
    tb = request.args.get('throwback', 'false')

    if request.args.get('roll'):
        seed_val = request.args.get('roll')
    else:
        return redirect('bravery?roll=' + gen_seed() + '&unified=' + ign_cls + '&low_pop=' + low_pop + '&throwback=' + tb)

    roller.roll(
            throwback = eval_bool_string(tb),
            seed = seed_val,
            ignore_class = eval_bool_string(ign_cls),
            exclude_low = eval_bool_string(low_pop)
        )
    return render_template('roll_result.html', result=roller, ignore=ign_cls, low=low_pop, throw=tb)

if __name__ == '__main__':
    app.run()
