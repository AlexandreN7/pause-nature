#!/usr/bin/env python
# -*- coding : utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("fr/index.html")
    
@app.route("/fr/")
def root_fr():
    return render_template("fr/index.html")
    
@app.route("/en/")
def root_en():
    return render_template("en/index.html")

@app.route("/home")
def home():
    return render_template("fr/index.html")
    
    
    

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
def gallery():
    return render_template("galerie_peinture.html")
   
@app.route("/galerie_pictures")
def gallery_pictures():
    return render_template("galerie_pictures.html") 

@app.route("/sheet-<name>")
def pic_gallery(name):
    html_name = "sheet-"+name+".html"
    return render_template(html_name)
    
@app.route("/sitemap")
def sitemap():
    return render_template("sitemap.xml")

if __name__ == "__main__" :
    app.run()

