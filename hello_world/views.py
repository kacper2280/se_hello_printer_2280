from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Aleksander"
moje_nazwisko = "Buczek"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie, moje_nazwisko,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
