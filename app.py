import os
from flask import Flask,  render_template
from keyDataClass import KeyDataConn
import json

app = Flask(__name__)

@app.route('/')
def getDBData():
    conn = KeyDataConn('Personstate.db')
    exec = conn.getAllUserData()
    return render_template('index.html',len=len(exec), data=exec)


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = os.urandom(64)
    app.config['FLASK_DEBUG'] = 1
    app.run()