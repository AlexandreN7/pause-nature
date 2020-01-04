#!/usr/bin/env python
# -*- coding : utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/home")
def reviews():
    return render_template("index.html")

@app.route("/review/<name>")
def review(name):
    htmlname = "review_"+name+".html"
    return render_template(htmlname)


@app.route("/ongoing")
def ongoing():
    return render_template("ongoing.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/galerie_peinture")
def galery():
    return render_template("galerie_peinture.html")

if __name__ == "__main__" :
    app.run()

