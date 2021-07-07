from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/feed-page")
def feed_page():
    return render_template("feed.html")

if __name__ == '__main__':
    app.run(debug=True)
