#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
import re 
import generate_pictures
import generate_paintings

#site_configuration = open("site_conf.txt","r")

os.system('rm templates/sheet-*'); # to be kept
generate_pictures.gene_pic_gallery()
generate_paintings.gene_pic_gallery()

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
"revue-rando-Fourchu",
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


#generation des articles anglais
for article in article_list_en :
   #Creation du fichier html
   template = open("templates/template_en.html", "r")
   file_html=open("templates/en/"+article+".html","w")
   print("Generation article :", article)
   #lecture du template

   #Generation des articles en anglais
   for ligne in template :
      file_article = open("reviews/en/"+article+".txt", "r")
      if "</head>" in ligne : #insertion du <head>
         #attention il y a un piege ici : l'article est genere ici /review/
         file_html.write('<link rel="alternate" hreflang="en" href="www.pause-nature.fr/review/'+article+'">')
         file_html.write('<script type="application/ld+json">')
         file_html.write('{')
         file_html.write('"@context" : "http://schema.org",')
         file_html.write('"@type" : "Article",')
         file_html.write('"name" : "'+article+'",')
         file_html.write('"author" : {')
         file_html.write('"@type" : "Person",')
         file_html.write('"name" : "Alexandre Proux"')
         file_html.write('},')
         file_html.write('"articleSection" : "review"')
         file_html.write('}')
         file_html.write('</script>')
         file_html.write('link rel="shortcut icon" type="image/ico" href="/static/img/favicon.ico"')

         write = 0
         for ligne_article in file_article :
            if "start_head" in ligne_article :
               write = 1
            if "end_head" in ligne_article :
               write = 0
            if write == 1 :
               print("ecriture du header")
               print(ligne_article)
               file_html.write(ligne_article)#ecriture de l'article


      if "content_beginning" in ligne : #insertion de l'article
         file_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
         file_html.write('<div>')

         for ligne_article in file_article :
            file_html.write(ligne_article)#ecriture de l'article
      file_article.close()

      file_html.write(ligne)#ecriture des lignes du templates
   file_html.close()
   template.close()

#generation des articles francais
for article in article_list_fr :
   #Creation du fichier html
   template = open("templates/template_fr.html", "r")
   file_html=open("templates/fr/"+article+".html","w")
   print("Generation article :", article)

   #Generation des articles en anglais
   for ligne in template :
      file_article = open("reviews/fr/"+article+".txt", "r")
      if "</head>" in ligne : #insertion du <head>
         #attention il y a un piege ici : l'article est genere ici /review/
         file_html.write('<link rel="alternate" hreflang="fr" href="www.pause-nature.fr/revue/'+article+'">')
         file_html.write('<script type="application/ld+json">')
         file_html.write('{')
         file_html.write('"@context" : "http://schema.org",')
         file_html.write('"@type" : "Article",')
         file_html.write('"name" : "'+article+'",')
         file_html.write('"author" : {')
         file_html.write('"@type" : "Person",')
         file_html.write('"name" : "Alexandre Proux"')
         file_html.write('},')
         file_html.write('"articleSection" : "review"')
         file_html.write('}')
         file_html.write('</script>')
         file_html.write('<link rel="shortcut icon" type="image/ico" href="/static/img/favicon.ico">')
         
         write = 0
         for ligne_article in file_article :
            if "start_head" in ligne_article :
               write = 1
            if "end_head" in ligne_article :
               write = 0
            if write == 1 :
               print("ecriture du header")
               print(ligne_article)
               file_html.write(ligne_article)#ecriture de l'article


      if "content_beginning" in ligne : #insertion de l'article
         file_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
         file_html.write('<div>')
         file_html.write('\n')
         
         for ligne_article in file_article :
         
            if "ads_reference" in ligne_article : # insertion d'une publicité
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
         
            file_html.write(ligne_article)#ecriture de l'article
      file_article.close()

      file_html.write(ligne)#ecriture des lignes du templates
   file_html.close()
   template.close()




#generation de l'index EN
index_html=open("templates/en/index.html","w")
print("Generation de l'index :")
template = open("templates/template_en.html", "r")
for ligne in template :
   if "</head>" in ligne : #insertion du <head>
      index_html.write('<meta name="p:domain_verify" content="cea44afbf402c3b5741620e0e26796e7"/>')
      index_html.write('\n')
      index_html.write('<meta name="description" content="Promoting a positive culture through articles on art, photography and paint. This website offers articles, tutorials and reviews on for drawer and watercolorist.">')#du titre
      index_html.write('\n')
      index_html.write('<title>Pause nature - The website dedicated to paint and nature</title>')#du titre
      index_html.write('\n')
      index_html.write('<link rel="alternate" hreflang="en" href="www.pause-nature.fr">')
      index_html.write('<link rel="shortcut icon" type="image/ico" href="/static/img/favicon.ico">')

   if "content_beginning" in ligne : #debut index
      index_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
      index_html.write('<h1 class="post-title">News</h1>')
      for article in article_list_en :
         index_html.write('<a href=/en/review/'+article+' >')
         file_article = open("reviews/en/"+article+".txt", "r")
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


#generation de l'index FR
index_html=open("templates/fr/index.html","w")
print("Generation de l'index :")
template = open("templates/template_fr.html", "r")
for ligne in template :
   if "</head>" in ligne : #insertion du <head>
      index_html.write('<meta name="p:domain_verify" content="cea44afbf402c3b5741620e0e26796e7"/>')
      index_html.write('\n')
      index_html.write('<meta name="description" content="Prenez votre appareil photo, votre peinture et partez sur des chemins de randonnées fantastiques sélectionnés par nos soins !">')#du titre
      index_html.write('\n')
      index_html.write('<title>Randonnée et peinture - pause nature</title>')#du titre
      index_html.write('\n')
      index_html.write('<link rel="alternate" hreflang="fr" href="www.pause-nature.fr">')
      index_html.write('<link rel="shortcut icon" type="image/ico" href="/static/img/favicon.ico">')
      index_html.write('')

   if "content_beginning" in ligne : #debut index
      index_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
      index_html.write('<h1 class="post-title">A la Une</h1>')
      for article in article_list_fr :
         index_html.write('<a href=/fr/revue/'+article+' >')
         file_article = open("reviews/fr/"+article+".txt", "r")
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


