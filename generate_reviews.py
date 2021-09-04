#!/usr/bin/env python
# -*- coding : utf-8 -*-

def gen_reviews_page(article_list_en, article_list_fr):
    """!
    """
    
    #generation de de l'onglet reviews EN
    review_html=open("templates/reviews.html","w")
    print("Generation de l'index :")
    template = open("templates/template_fr.html", "r")
    for ligne in template :
        if "</head>" in ligne : #insertion du <head>
            review_html.write('<meta name="description" content="Cette page contient la liste des articles publiés sur les thêmes de la randonnée, du dessin et de la peinture aquarelle">  ')#du titre
            review_html.write('<title>Archive des articles</title>')#du titre
            review_html.write('<link rel="alternate" hreflang="en" href="http://www.pause-nature.fr/reviews">')
            review_html.write('<link rel="shortcut icon" type="image/ico" href="/static/img/favicon.ico">')

        if "content_beginning" in ligne : #debut index
            review_html.write('<div class="content pure-u-1 pure-u-md-3-4">')

            for article in article_list_fr :
                review_html.write('<a href=/fr/revue/'+article+' >')
                review_html.write('<p>'+article+'</p>')
                review_html.write('</a>')
            review_html.write('<br>')
            review_html.write('<br>')
            for article in article_list_en :
                review_html.write('<a href=/en/review/'+article+' >')
                review_html.write('<p>'+article+'</p>')
                review_html.write('</a>')

        review_html.write(ligne)#ecriture des lignes du templates
    review_html.close()
    template.close()
