#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
#os.chdir("C:/tests python")

#site_configuration = open("site_conf.txt","r")

article_list = [
"review_versatile_palette",
"review_morikuni",
"review_hahnemuhle_watercolor_book",
"review_kuretake_gansai_tambi",
"review_hiroshige",
"review_black_ink",
"review_portable_painter"
]



#generation des articles
for article in article_list :
   #Creation du fichier html
   template = open("templates/template.html", "r")
   file_html=open("templates/"+article+".html","w")
   print("Generation article :", article)
   #lecture du template
	
   for ligne in template :
      file_article = open("reviews/"+article+".txt", "r")
      if "</head>" in ligne : #insertion du <head>
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



#generation de l'index

index_html=open("templates/index.html","w")
print("Generation de l'index :")
template = open("templates/template.html", "r")
for ligne in template :
   if "</head>" in ligne : #insertion du <head>
      index_html.write('<meta name="description" content="Promoting a positive culture through articles on art, photography and paint.">  ')#du titre
      index_html.write('<title>Pause nature - The website dedicated to paint and nature</title>')#du titre
               
   if "content_beginning" in ligne : #debut index
      index_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
      for article in article_list :
         index_html.write('<a href=review/'+article+' >')
         file_article = open("reviews/"+article+".txt", "r")
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

#generation de l'index

review_html=open("templates/reviews.html","w")
print("Generation de l'index :")
template = open("templates/template.html", "r")
for ligne in template :
   if "</head>" in ligne : #insertion du <head>
      review_html.write('<meta name="description" content="Summary of reviews on the theme of art, watercolor and painting materials.">  ')#du titre
      review_html.write('<title>List of review</title>')#du titre
               
   if "content_beginning" in ligne : #debut index
      review_html.write('<div class="content pure-u-1 pure-u-md-3-4">')
      for article in article_list :
         review_html.write('<a href=review/'+article+' >')
         review_html.write('<p>'+article+'</p>')
         review_html.write('</a>')

   review_html.write(ligne)#ecriture des lignes du templates
review_html.close()	
template.close()