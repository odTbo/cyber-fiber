from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/feed-page")
def feed_page():
    return render_template("feed.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/new-post')
def new_post():
    return render_template('new_post.html')


if __name__ == '__main__':
    app.run(debug=True)
