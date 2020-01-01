#!/usr/bin/env python
# -*- coding : utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", message = "hello world")

@app.route("/home")
def reviews():
    return render_template("home.html", message = "hello world")

@app.route("/reviews/<review_name>")
def review(name):
    return render_template("index.html", message = "hello world")


@app.route("/galerie_peinture")
def galery():
    return render_template("galerie_peinture.html", message = "hello world")

if __name__ == "__main__" :
    app.run()

