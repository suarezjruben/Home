import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return flask.render_template("index.html")


@app.route('/index.html')
def home():  # put application's code here
    return flask.render_template("index.html")


@app.route('/education.html')
def education():
    return flask.render_template("education.html")


@app.route('/work_experience.html')
def work():
    return flask.render_template("work_experience.html")


@app.route('/resume.html')
def resume():
    return flask.render_template("resume.html")


if __name__ == '__main__':
    app.run()
