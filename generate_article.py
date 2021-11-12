#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
import re 
import generate_pictures
import generate_paintings
import generate_reviews
from random import randint

#site_configuration = open("site_conf.txt","r")

os.system('rm -f templates/sheet-*'); # to be kept
generate_paintings.gene_pic_gallery()
generate_pictures.gene_pic_gallery()

article_list_en = [
"review-Saal",
"review-manet-ukiyoe",
"review-fountain-pen-lamy2000",
"review-versatile-palette",
"review-morikuni",
"review-hahnemuhle-watercolor-book",
"review-kuretake-gansai-tambi",
"review-hiroshige",
"review-black-ink",
"review-portable-painter"
]

article_list_fr = [
"revue-rando-Valgaudemar",
"revue-rando-Fourchu",
"revue-rando-St-Cirq-Lapopie",
"revue-rando-Perollier",
"revue-rando-Dourgne",
"revue-rando-Caylus",
"revue-rando-Charlet",
"revue-rando-salette",
"revue-rando-valjouffrey",
"revue-rando-connex",
"revue-rando-passerelles",
"revue-rando-lac-mort",
"revue-rando-chauvet",
"revue-rando-Pellafol",
"revue-champignons",
"revue-rando-cancale",
"revue-Saal",
"revue-rando-Prapic",
"revue-tutoriel-fabrication-aquarelle",
"revue-rando-Ambialet",
"revue-rando-bruniquel",
"revue-rando-beynes",
"revue-tendre-le-papier",
"revue-ponsonnas",
"revue-rando-montfort",
"revue-kuretake-gansai-tambi",
"revue-fountain-pen-lamy2000",
"revue-portable-painter",
"revue-black-ink"
]

definitions = {
    "en":
        {
            "name":"review",
            "dict":article_list_en,
        },
    "fr": 
        {
            "name":"revue",
            "dict":article_list_fr,            
        },
    
    }
HEAD_INSERT_PATTERN="INSERT HEAD"

for langue in definitions.keys():
    for article in definitions[langue]["dict"]:
        #Creation du fichier html
        template = open("templates/template_"+langue+".html", "r")
        file_html=open("templates/"+langue+"/"+article+".html","w")
        print("Generation article :", article)
        file_article = open("reviews/"+langue+"/"+article+".txt", "r")
        add_ads = True

        HEAD_TXT = "<link rel=\"alternate\" hreflang=\""+langue+"\" href=\"www.pause-nature.fr/"+definitions[langue]["name"]+"/"+article+"\"><script type=\"application/ld+json\">{\"@context\" : \"http://schema.org\",\"@type\" : \"Article\",\"name\" : \""+article+"\",\"author\" : {\"@type\" : \"Person\",\"name\" : \"Alexandre Proux\"},\"articleSection\" : \"review\"}</script><link rel=\"shortcut icon\" type=\"image/ico\" href=\"/static/img/favicon.ico\">"

        #Generation des articles en anglais
        for ligne_template in template :
            # Print header 
            if HEAD_INSERT_PATTERN in ligne_template : #insertion du <head>
                file_html.write(HEAD_TXT)
                file_html.write("\n")

                write = 0
                for ligne_article in file_article :
                    if "start_head" in ligne_article :
                        write = 1
                    if "end_head" in ligne_article :
                        break
                    if write == 1 :
                        file_html.write(ligne_article)#ecriture de l'article
                continue

            # Print content 
            if "content_beginning" in ligne_template : #insertion de l'article
                #file_html.write('<div class="content pure-u-1 pure-u-md-3-4">\n')

                for ligne_article in file_article :
                    file_html.write(ligne_article)#ecriture de l'article
                    
                    ads = randint(0,100)
                    if (((ads%2) == 0) and add_ads and (ligne_template == "")):
                        add_ads = False
                        print("insertion d'une pub")
                        #Generation des pubs pour google
                        file_html.write("\n")
                        file_html.write('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>' + "\n")
                        file_html.write('<ins class="adsbygoogle"'+ "\n")
                        file_html.write('style="display:block; text-align:center;"'+ "\n")
                        file_html.write('data-ad-layout="in-article"'+ "\n")
                        file_html.write('data-ad-format="fluid"'+ "\n")
                        file_html.write(' data-ad-client="ca-pub-4353004932795007"'+ "\n")
                        file_html.write('data-ad-slot="5273903670"></ins>'+ "\n")
                        file_html.write('<script>'+ "\n")
                        file_html.write('(adsbygoogle = window.adsbygoogle || []).push({});'+ "\n")
                        file_html.write('</script>'+ "\n")
                        file_html.write("\n")                
                
                continue
                    
            # Ecriture du template après avoir écrit le morceau d'article 
            file_html.write(ligne_template)

        file_article.close()
        file_html.close()
        template.close()

for langue in definitions.keys():
    #generation de l'index EN
    index_html=open("templates/"+langue+"/index.html","w")
    print("Generation de l'index :")
    template = open("templates/template_"+langue+".html", "r")
    for ligne in template :
        if HEAD_INSERT_PATTERN in ligne : #insertion du <head>
            index_html.write('<meta name="p:domain_verify" content="cea44afbf402c3b5741620e0e26796e7"/>')
            index_html.write('\n')
            index_html.write('<meta name="description" content="Promoting a positive culture through articles on art, photography and paint. This website offers articles, tutorials and reviews on for drawer and watercolorist.">')#du titre
            index_html.write('\n')
            index_html.write('<title>Pause nature - The website dedicated to paint and nature</title>')#du titre
            index_html.write('\n')
            index_html.write('<link rel="alternate" hreflang="'+langue+'" href="www.pause-nature.fr">')
            index_html.write('<link rel="shortcut icon" type="image/ico" href="/static/img/favicon.ico">')

        if "content_beginning" in ligne : #debut index
            if (langue == 'en'):
                index_html.write('<h1 class="post-title">News</h1>')
            else:
                index_html.write('<h1 class="post-title">A la Une</h1>')
            for article in definitions[langue]["dict"] :
                index_html.write('<a href=/'+langue+'/'+definitions[langue]["name"]+'/'+article+' >')
                file_article = open("reviews/"+langue+"/"+article+".txt", "r")
                for ligne_article in file_article :
                    if "start_head" in ligne_article :
                        write = 0
                    if "end_head" in ligne_article :
                        write = 1
                    if write == 1 :

                        if "end_header" in ligne_article :
                            index_html.write('<p>...</p>')
                            index_html.write('</div>')
                            index_html.write('</section>')
                            break
                        else :
                            new_line = ligne_article.replace("h1","h2")
                            index_html.write(new_line)
                index_html.write('</a>')

        index_html.write(ligne)#ecriture des lignes du templates
        
    index_html.close()
    template.close()


#generation de la table des article
generate_reviews.gen_reviews_page(article_list_en, article_list_fr)


