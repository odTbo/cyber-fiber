from flask import Flask, render_template, url_for, request
from forms import RegisterForm, LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "12345"


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/feed-page")
def feed_page():
    return render_template("feed.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        email = form.email.data
        password = form.password.data
        print(email, password)

    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and request.method == "POST":
        email = form.email.data
        age = form.age.data
        password = form.password.data
        print(email, age, password)

    return render_template('register.html', form=form)


@app.route('/new-post')
def new_post():
    return render_template('new_post.html')


if __name__ == '__main__':
    app.run(debug=True)
