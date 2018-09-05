'''
Created on 2018/09/05

@author: user36-pci
'''
from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "hello, Flask!"



@app.route('/hello')
def hello():
    name = "Hello world!"
    return name

@app.route("/gotoPage")
def gotoPage():
    return render_template("thisPage.html")


if __name__ == "__main__":
    app.run()

