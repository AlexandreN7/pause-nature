#!/usr/bin/env python
# -*- coding : utf-8 -*-
import re 
import os

def gen_reviews_page(article_list_en, article_list_fr):
    """!
    """
    
    rando = {}
    art = {}
    all_elements = {}
    
    #
    # Save FR articles info
    #
    for article in article_list_fr :
        # Open the article file and get information
        current_article_path = "reviews/fr/"+article+".txt"
        current_article = open(current_article_path, "r")                
        new_dict = {
            "title" : None,
            }
        new_dict["lang"] = "fr/revue"
        rando_type = 0
        for ar_line in current_article.readlines():
            match = re.findall(r'post-title\">(.*)<', ar_line)
            if (match != []): # Found the title
                new_dict["title"] = str(match[0])
                
            # Differenciate hike from art reviews
            # This part shall be the last before changing article 
            # This is the first line of the article, we do get into this again
        
            match = re.findall("RANDO_KEYWORD", ar_line)
            if (match != []): # Found a rando 
                rando_type = 1
                
        if (rando_type == 1): # Found a rando 
            rando[article] = new_dict.copy()
        else:
            art[article] = new_dict.copy()
            
        all_elements[article] = new_dict.copy()
        current_article.close()
     
    #
    # Save EN articles info
    #
    for article in article_list_en:
        # Open the article file and get information
        current_article_path = "reviews/en/"+article+".txt"
        current_article = open(current_article_path, "r")                
        new_dict = {
            "title" : None,
            }
        new_dict["lang"] = "en/review"
        rando_type = 0
        for ar_line in current_article.readlines():
            match = re.findall(r'post-title\">(.*)<', ar_line)
            if (match != []): # Found the title
                new_dict["title"] = match[0]
                
            # Differenciate hike from art reviews
            # This part shall be the last before changing article 
            # This is the first line of the article, we do get into this again
        
            match = re.findall("RANDO_KEYWORD", ar_line)
            if (match != []): # Found a rando 
                rando_type = 1
                
        if (rando_type == 1): # Found a rando 
            rando[article] = new_dict.copy()
        else:
            art[article] = new_dict.copy()
            
        all_elements[article] = new_dict.copy()
        current_article.close()       
       
    #
    # Create the reviews page
    #
    generate_reviews_page("reviews",all_elements)
    generate_reviews_page("reviews_art",art)
    generate_reviews_page("reviews_rando",rando)


def generate_reviews_page(page_name, dictionnary):
    reviews_to_create = "templates/"+str(page_name)+".html"
    review_html=open(reviews_to_create,"r")
    temporary_file_name = "templates/reviews_temp.txt"
    temporary = open(temporary_file_name, "w")
    copy = 1 # Start with copying the lines 
    for line in review_html.readlines():
        if copy==1: # Copy lines 
            temporary.write(line)
        
        if (re.search("end autogenerated", line)):
            copy = 1
            temporary.write(line) # Copy "end autogenerated"
    
        if (re.search("start autogenerated", line)):
            copy = 0    # Stop copying to add new lines 
            # Add here new lines
           
            temporary.write("Filres/Filters :     <a href=\"/reviews\" class=\"buttonPage\">Tous/All</a>\n")
            temporary.write("<a href=\"/reviews_art\" class=\"buttonPage\">Art</a>\n")
            temporary.write("<a href=\"/reviews_rando\" class=\"buttonPage\">Randonnées/Hikes</a></p>\n")
                        
            temporary.write("\t<table>\n\t\t<thead>\n\t\t\t<tr>\n\t\t\t\t<th colspan=\"2\" bgcolor=\"#808080\">Articles</th>\n\t\t\t</tr>\n\t\t</thead>\n")
            temporary.write("\t<tbody>\n")
            cnt = 0
            for article in dictionnary.keys():
                # First line 
                if ((cnt%2)==0): # new line 
                    if (cnt != 0):
                        temporary.write("\t\t</tr>\n") # end previous line
                    temporary.write("\t\t<tr>\n") # New line 
                temporary.write("\t\t\t<td>\n")
                # The table body
                temporary.write("\t\t\t\t<a href=/"+str(dictionnary[article]["lang"])+"/"+str(article)+"><p>"+str(dictionnary[article]["title"])+"</p></a>\n")
                temporary.write("\t\t\t</td>\n")
                cnt = cnt +1
            temporary.write("\t</tbody>\n\t</table>\n")                        

    review_html.close()
    temporary.close()
    os.system("mv "+temporary_file_name+" "+reviews_to_create)        
