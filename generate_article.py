#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
#os.chdir("C:/tests python")

#site_configuration = open("site_conf.txt","r")

article_list_en = [
"review_manet_ukiyoe",
"review_fountain_pen_lamy2000",
"review_versatile_palette",
"review_morikuni",
"review_hahnemuhle_watercolor_book",
"review_kuretake_gansai_tambi",
"review_hiroshige",
"review_black_ink",
"review_portable_painter"
]

article_list_fr = [
"revue_kuretake_gansai_tambi",
"revue_fountain_pen_lamy2000",
"revue_portable_painter",
"revue_black_ink",
"revue_rando_montfort"
]


#generation des articles anglais
for article in article_list_en :
   #Creation du fichier html
   template = open("templates/template.html", "r")
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
   template = open("templates/template.html", "r")
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
   
   


#generation de l'index EN
index_html=open("templates/en/index.html","w")
print("Generation de l'index :")
template = open("templates/template.html", "r")
for ligne in template :
   if "</head>" in ligne : #insertion du <head>
      index_html.write('<meta name="p:domain_verify" content="cea44afbf402c3b5741620e0e26796e7"/>')
      index_html.write('\n')
      index_html.write('<meta name="description" content="Promoting a positive culture through articles on art, photography and paint. This website offers articles, tutorials and reviews on for drawer and watercolorist.">')#du titre
      index_html.write('\n')
      index_html.write('<title>Pause nature - The website dedicated to paint and nature</title>')#du titre
      index_html.write('\n')
      index_html.write('<link rel="alternate" hreflang="en" href="www.pause-nature.fr">')
               
   if "content_beginning" in ligne : #debut index
      index_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
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
                   index_html.write(ligne_article)
         index_html.write('</a>')

   index_html.write(ligne)#ecriture des lignes du templates
index_html.close()	
template.close()

#generation de l'index FR
index_html=open("templates/fr/index.html","w")
print("Generation de l'index :")
template = open("templates/template.html", "r")
for ligne in template :
   if "</head>" in ligne : #insertion du <head>
      index_html.write('<meta name="p:domain_verify" content="cea44afbf402c3b5741620e0e26796e7"/>')
      index_html.write('\n')
      index_html.write('<meta name="description" content="Promoting a positive culture through articles on art, photography and paint. This website offers articles, tutorials and reviews on for drawer and watercolorist.">')#du titre
      index_html.write('\n')
      index_html.write('<title>Pause nature - The website dedicated to paint and nature</title>')#du titre
      index_html.write('\n')
      index_html.write('<link rel="alternate" hreflang="fr" href="www.pause-nature.fr">')
               
   if "content_beginning" in ligne : #debut index
      index_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
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
                   index_html.write(ligne_article)
         index_html.write('</a>')

   index_html.write(ligne)#ecriture des lignes du templates
index_html.close()	
template.close()

#generation de la table des article

#generation de de l'onglet reviews EN
review_html=open("templates/reviews.html","w")
print("Generation de l'index :")
template = open("templates/template.html", "r")
for ligne in template :
   if "</head>" in ligne : #insertion du <head>
      review_html.write('<meta name="description" content="Summary of reviews on the theme of art, watercolor and painting materials.">  ')#du titre
      review_html.write('<title>List of review</title>')#du titre
      review_html.write('<link rel="alternate" hreflang="en" href="http://www.pause-nature.fr/reviews">')
               
   if "content_beginning" in ligne : #debut index
      review_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
      for article in article_list_en :
         review_html.write('<a href=/en/review/'+article+' >')
         review_html.write('<p>'+article+'</p>')
         review_html.write('</a>')

   review_html.write(ligne)#ecriture des lignes du templates
review_html.close()	
template.close()