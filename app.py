# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Finally a flask in the dock container.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1062)
