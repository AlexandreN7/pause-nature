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
    
    
@app.route("/en/review/review-<name>")
def review(name):
    htmlname = "en/review-"+name+".html"
    return render_template(htmlname)
    
@app.route("/fr/revue/revue-<name>")
def revue(name):
    htmlname = "fr/revue-"+name+".html"
    return render_template(htmlname)
    
@app.route("/reviews")
def reviews():
    return render_template("reviews.html")

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
    
@app.route("/sitemap.xml")
def sitemap():
    return render_template("sitemap.xml")
    
@app.route("/robots.txt")
def robots():
    return render_template("robots.txt")
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404    

if __name__ == "__main__" :
    app.run()

