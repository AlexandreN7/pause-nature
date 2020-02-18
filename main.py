#!/usr/bin/env python
# -*- coding : utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/en/review/review_<name>")
def review(name):
    htmlname = "en/review_"+name+".html"
    return render_template(htmlname)
    
@app.route("/fr/revue/revue_<name>")
def revue(name):
    htmlname = "fr/revue_"+name+".html"
    return render_template(htmlname)
    
@app.route("/reviews")
def reviews():
    return render_template("reviews.html")

@app.route("/ongoing")
def ongoing():
    return render_template("ongoing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/galerie_peinture")
def galery():
    return render_template("galerie_peinture.html")
    
@app.route("/sitemap")
def sitemap():
    return render_template("sitemap.xml")

if __name__ == "__main__" :
    app.run()

