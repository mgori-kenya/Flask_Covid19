# Import flask
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def index():
    return "Hello World"


@app.route('/greetings/<name>')
def greetings(name):
    return "Hello" + name


if __name__ == '__main__':
    app.run(debug=True, port=5000)
