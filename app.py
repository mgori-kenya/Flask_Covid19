# Import flask
from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'id':1,'name':'salma','language':'javascript'},
    {'id':2,'name':'mathew','language':'java'},
    {'id':3,'name':'James','language':'kotlin'},
    {'id':4,'name': 'Lewis','language': 'python'}
]

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return render_template("index.html", watu=users)


@app.route('/greetings/<name>')
def greetings(name):
    return render_template("greetings.html")

@app.route('/getid/<int:user_id>')
def get_user_id(user_id):
    #response must be sting, tuple in response
    return render_template("get user.html")


@app.route('/users/<int:user_id>')
def get_user_id(user_id):
    for user in users: #loops through all users in list
        if user['id'] ==user_id: #gets user with specific id
            user_name = user('name')

            return render_template("get_user.html", found_user=user_name)
        else:
            return "user not found"


# 200: everything ok
# 201: data created successfully
# 404: page not found
# 500: internal server error

@app.errorhandler(404)
def not_found(error):
    return "kuna shida kwa server: {}".format(error),404


@app.errorhandler(500)
def internal_error(error):
    return "There is an internal server error: {}".format(error), 500


if __name__ == '__main__':
    app.run(debug=False, port=5000)





