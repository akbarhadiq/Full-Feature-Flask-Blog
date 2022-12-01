from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from load_dotenv import load_dotenv
import os

app=Flask(__name__)


load_dotenv('environ.env')
secret_key = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = secret_key

posts = [
    {
        'author': 'Akbar Hadiq',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted': 'April 20, 2018'
    },

    {
        'author': 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# you can use double routes
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html', title='Login', form=form)

# flask auto run when script run:
if __name__ == "__main__":
    app.run(debug=True)