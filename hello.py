from flask import Flask
from flask import request
from flask import render_template

from markupsafe import escape

app = Flask("__name__")

@app.route("/")
def index():
    return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name=None):
    return render_template('hello.html', name = name)


if __name__ == "__main__": app.run(host="0.0.0.0", port=9000) # host주소와 port number 선언

