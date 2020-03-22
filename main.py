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

@app.route("/sheet_bee-4944489_960_720")
def test_bee_4944489_960_720():
    return render_template("sheet_bee-4944489_960_720.html")

@app.route("/sheet_bee-4944485_960_720")
def test_bee_4944485_960_720():
    return render_template("sheet_bee-4944485_960_720.html")

@app.route("/sheet_bee-4944486_960_720")
def test_bee_4944486_960_720():
    return render_template("sheet_bee-4944486_960_720.html")

@app.route("/sheet_butterfly-4951289_960_720")
def test_butterfly_4951289_960_720():
    return render_template("sheet_butterfly-4951289_960_720.html")

@app.route("/sheet_bulrush-4951322_960_720")
def test_bulrush_4951322_960_720():
    return render_template("sheet_bulrush-4951322_960_720.html")

@app.route("/sheet_butterfly-4951309_960_720")
def test_butterfly_4951309_960_720():
    return render_template("sheet_butterfly-4951309_960_720.html")

@app.route("/sheet_butterfly-4951310_960_720")
def test_butterfly_4951310_960_720():
    return render_template("sheet_butterfly-4951310_960_720.html")

@app.route("/sheet_flowers-4951325_960_720")
def test_flowers_4951325_960_720():
    return render_template("sheet_flowers-4951325_960_720.html")

@app.route("/sheet_bee-4944487_960_720")
def test_bee_4944487_960_720():
    return render_template("sheet_bee-4944487_960_720.html")

@app.route("/sheet_flowers-4951286_960_720")
def test_flowers_4951286_960_720():
    return render_template("sheet_flowers-4951286_960_720.html")

@app.route("/sheet_flowers-4951332_960_720")
def test_flowers_4951332_960_720():
    return render_template("sheet_flowers-4951332_960_720.html")

@app.route("/sheet_bird-4930603_960_720")
def test_bird_4930603_960_720():
    return render_template("sheet_bird-4930603_960_720.html")

@app.route("/sheet_duck-4926219_960_720")
def test_duck_4926219_960_720():
    return render_template("sheet_duck-4926219_960_720.html")

@app.route("/sheet_lizard-4941499_960_720")
def test_lizard_4941499_960_720():
    return render_template("sheet_lizard-4941499_960_720.html")

@app.route("/sheet_flower-4944491_960_720")
def test_flower_4944491_960_720():
    return render_template("sheet_flower-4944491_960_720.html")

@app.route("/sheet_lizard-4941507_960_720")
def test_lizard_4941507_960_720():
    return render_template("sheet_lizard-4941507_960_720.html")

@app.route("/sheet_moutain-4941506_960_720")
def test_moutain_4941506_960_720():
    return render_template("sheet_moutain-4941506_960_720.html")

@app.route("/sheet_lizard-4941501_960_720")
def test_lizard_4941501_960_720():
    return render_template("sheet_lizard-4941501_960_720.html")

@app.route("/sheet_mushrooms-4873141_960_720")
def test_mushrooms_4873141_960_720():
    return render_template("sheet_mushrooms-4873141_960_720.html")

@app.route("/sheet_leaves-4873125_960_720")
def test_leaves_4873125_960_720():
    return render_template("sheet_leaves-4873125_960_720.html")

@app.route("/sheet_moutain-4941509_960_720")
def test_moutain_4941509_960_720():
    return render_template("sheet_moutain-4941509_960_720.html")

@app.route("/sheet_duck-4873132_960_720")
def test_duck_4873132_960_720():
    return render_template("sheet_duck-4873132_960_720.html")

@app.route("/sheet_goose-4873142_960_720")
def test_goose_4873142_960_720():
    return render_template("sheet_goose-4873142_960_720.html")

@app.route("/sheet_tulip-4879970_960_720")
def test_tulip_4879970_960_720():
    return render_template("sheet_tulip-4879970_960_720.html")

@app.route("/sheet_flowers-4873131_960_720")
def test_flowers_4873131_960_720():
    return render_template("sheet_flowers-4873131_960_720.html")

@app.route("/sheet_cat-4774164_960_720")
def test_cat_4774164_960_720():
    return render_template("sheet_cat-4774164_960_720.html")

@app.route("/sheet_versailles-4873133_960_720")
def test_versailles_4873133_960_720():
    return render_template("sheet_versailles-4873133_960_720.html")

@app.route("/sheet_tulip-4879969_960_720")
def test_tulip_4879969_960_720():
    return render_template("sheet_tulip-4879969_960_720.html")

@app.route("/sheet_mushroom-4686877_960_720")
def test_mushroom_4686877_960_720():
    return render_template("sheet_mushroom-4686877_960_720.html")

@app.route("/sheet_mushroom-4693264_960_720")
def test_mushroom_4693264_960_720():
    return render_template("sheet_mushroom-4693264_960_720.html")

@app.route("/sheet_mushroom-4655464_960_720")
def test_mushroom_4655464_960_720():
    return render_template("sheet_mushroom-4655464_960_720.html")

@app.route("/sheet_flowers-4873127_960_720")
def test_flowers_4873127_960_720():
    return render_template("sheet_flowers-4873127_960_720.html")

@app.route("/sheet_mushrooms-4655480_960_720")
def test_mushrooms_4655480_960_720():
    return render_template("sheet_mushrooms-4655480_960_720.html")

@app.route("/sheet_sun-4731859_960_720")
def test_sun_4731859_960_720():
    return render_template("sheet_sun-4731859_960_720.html")

@app.route("/sheet_mushroom-4655463_960_720")
def test_mushroom_4655463_960_720():
    return render_template("sheet_mushroom-4655463_960_720.html")

@app.route("/sheet_mushrooms-4693269_960_720")
def test_mushrooms_4693269_960_720():
    return render_template("sheet_mushrooms-4693269_960_720.html")

@app.route("/sheet_mushroom-4655479_960_720")
def test_mushroom_4655479_960_720():
    return render_template("sheet_mushroom-4655479_960_720.html")

@app.route("/sheet_hephaistos-temple-4673515_960_720")
def test_hephaistos_temple_4673515_960_720():
    return render_template("sheet_hephaistos-temple-4673515_960_720.html")

@app.route("/sheet_mushroom-4655429_960_720")
def test_mushroom_4655429_960_720():
    return render_template("sheet_mushroom-4655429_960_720.html")

@app.route("/sheet_marigold-4655440_960_720")
def test_marigold_4655440_960_720():
    return render_template("sheet_marigold-4655440_960_720.html")

@app.route("/sheet_passionflower-4774160_960_720")
def test_passionflower_4774160_960_720():
    return render_template("sheet_passionflower-4774160_960_720.html")

@app.route("/sheet_marigolds-4655449_960_720")
def test_marigolds_4655449_960_720():
    return render_template("sheet_marigolds-4655449_960_720.html")

@app.route("/sheet_mushrooms-4663017_960_720")
def test_mushrooms_4663017_960_720():
    return render_template("sheet_mushrooms-4663017_960_720.html")

@app.route("/sheet_mushroom-4655423_960_720")
def test_mushroom_4655423_960_720():
    return render_template("sheet_mushroom-4655423_960_720.html")

@app.route("/sheet_moss-4693294_960_720")
def test_moss_4693294_960_720():
    return render_template("sheet_moss-4693294_960_720.html")

@app.route("/sheet_flowers-4873128_960_720")
def test_flowers_4873128_960_720():
    return render_template("sheet_flowers-4873128_960_720.html")

@app.route("/sheet_sun-4673483_960_720")
def test_sun_4673483_960_720():
    return render_template("sheet_sun-4673483_960_720.html")

@app.route("/sheet_cat-4662991_960_720")
def test_cat_4662991_960_720():
    return render_template("sheet_cat-4662991_960_720.html")

@app.route("/sheet_parakeet-4662983_960_720")
def test_parakeet_4662983_960_720():
    return render_template("sheet_parakeet-4662983_960_720.html")

@app.route("/sheet_mushroom-4655468_960_720")
def test_mushroom_4655468_960_720():
    return render_template("sheet_mushroom-4655468_960_720.html")

@app.route("/sheet_mushroom-4655434_960_720")
def test_mushroom_4655434_960_720():
    return render_template("sheet_mushroom-4655434_960_720.html")

@app.route("/sheet_cat-4663020_960_720")
def test_cat_4663020_960_720():
    return render_template("sheet_cat-4663020_960_720.html")

@app.route("/sheet_bird-4731870_960_720")
def test_bird_4731870_960_720():
    return render_template("sheet_bird-4731870_960_720.html")

@app.route("/sheet_art-4673516_960_720")
def test_art_4673516_960_720():
    return render_template("sheet_art-4673516_960_720.html")

@app.route("/sheet_nature-4673503_960_720")
def test_nature_4673503_960_720():
    return render_template("sheet_nature-4673503_960_720.html")

@app.route("/sheet_mushroom-4673519_960_720")
def test_mushroom_4673519_960_720():
    return render_template("sheet_mushroom-4673519_960_720.html")

@app.route("/sheet_ancient-agora-4662993_960_720")
def test_ancient_agora_4662993_960_720():
    return render_template("sheet_ancient-agora-4662993_960_720.html")

@app.route("/sheet_mushroom-4673410_960_720")
def test_mushroom_4673410_960_720():
    return render_template("sheet_mushroom-4673410_960_720.html")

@app.route("/sheet_nature-4673499_960_720")
def test_nature_4673499_960_720():
    return render_template("sheet_nature-4673499_960_720.html")

@app.route("/sheet_mushroom-4662970_960_720")
def test_mushroom_4662970_960_720():
    return render_template("sheet_mushroom-4662970_960_720.html")

@app.route("/sheet_mountains-4941503_960_720")
def test_mountains_4941503_960_720():
    return render_template("sheet_mountains-4941503_960_720.html")

@app.route("/sheet_caterpillar-4941500_960_720")
def test_caterpillar_4941500_960_720():
    return render_template("sheet_caterpillar-4941500_960_720.html")

@app.route("/sheet_flower-4944492_960_720")
def test_flower_4944492_960_720():
    return render_template("sheet_flower-4944492_960_720.html")
    
@app.route("/sitemap")
def sitemap():
    return render_template("sitemap.xml")

if __name__ == "__main__" :
    app.run()

