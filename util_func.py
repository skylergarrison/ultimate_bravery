import random

def gen_seed():
    return str(random.randint(1, 8783818952879679611000))

def eval_bool_string(string_input):
    if string_input == 'true':
        return True
    if string_input == 'false':
        return False