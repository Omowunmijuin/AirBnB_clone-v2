#!/usr/bin/python3
"""
Starting a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(id=None):
    """display the states and cities listed in alphabetical order"""
    if id:
        states = storage.all("State")
        key = 'State.' + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    else:
        states = list(storage.all(state).values())
    return render_template('9-states.html', state=state, states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
