from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/my_blog')
def my_blog():
    return 'Welcome to my blog Page!'
@app.route('/user/<user_name>')
def user_info(user_name):
    # return f"Welcome Back {user_name}"
    return render_template('index.html', user_name=user_name)