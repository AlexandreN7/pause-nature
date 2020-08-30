#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
import re 
#import deviantart library
import deviantart

######################################
### Create functions 
######################################
def autoHTML (name, link, alt, templatePath, pageURL):
    foFILE_sheet = open (templatePath+"/sheet-"+name+".html", "w")
    foFILE_sheet.write("<!doctype html>\n")
    foFILE_sheet.write("<html lang=\"en\">\n")
    foFILE_sheet.write("    <head>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("    <script data-ad-client=\"ca-pub-4353004932795007\" async\n")
    foFILE_sheet.write("          src=\"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("   <meta name=\"google-site-verification\" content=\"9cZqCjgkf5l9r1cUe7kBRjXSj4Ru49PHJiXJmp96S7k\" />\n")
    foFILE_sheet.write("    <meta name=\"msvalidate.01\" content=\"ADBE1D6C621C0EE7980A84478EED53ED\" />\n")
    foFILE_sheet.write("    <meta charset=\"utf-8\">\n")
    foFILE_sheet.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    foFILE_sheet.write("    <link rel=\"stylesheet\" href=\"../static/css/layouts/pure-min.css\">\n")
    foFILE_sheet.write("    <link rel=\"stylesheet\" href=\"../static/css/layouts/grids-responsive-min.css\">\n")
    foFILE_sheet.write("    <link rel=\"stylesheet\" href=\"../static/css/layouts/blog.css\">\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("    <script type=\"application/ld+json\">{\"@context\" : \"http://schema.org\",\"@type\" : \"Article\",\"name\" : \"pictures\",\"author\" : {\"@type\" : \"Person\",\"name\" : \"Amandine Poterala\"},\"articleSection\" : \"Pictures\"}</script>\n")
    foFILE_sheet.write("    <meta name=\"description\" content=\"Amandine's pictures.\">\n")  
    foFILE_sheet.write("\n")
    foFILE_sheet.write("</head>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("<body>\n")
    foFILE_sheet.write("<div id=\"layout\" class=\"pure-g\">\n")
    foFILE_sheet.write("        <div class=\"sidebar pure-u-1 pure-u-md-1-5\">\n")
    foFILE_sheet.write("            <div class=\"header\">\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <p><center>\n")
    foFILE_sheet.write('                    <img width=\"140\" height=\"140\" alt=\"Alexandre Proux avatar\" src="/static/img/icon.jpg">\n')
    foFILE_sheet.write("                </center></p>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <h1 class=\"brand-title\">Pause nature</h1>\n")
    foFILE_sheet.write("                <h2 class=\"brand-tagline\">Nature, watercolor and photography</h2>\n")
    foFILE_sheet.write("                <h2 class=\"brand-tagline\"></h2>\n")
    foFILE_sheet.write("                <nav class=\"nav\">\n")
    foFILE_sheet.write("                    <ul class=\"nav-list\">\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/home\">Home</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/reviews\">Reviews</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/galerie_peinture\">Paintings</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/galerie_peinture\">Pictures</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/about\">About</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                    </ul>\n")
    foFILE_sheet.write("                </nav>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <p><center>\n")
    foFILE_sheet.write("                    <a href=\"https://www.instagram.com/archiwyzard/\"><img src=\"../static/img/common/logo_instagram.jpg\" alt=\"logo instagram\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://www.instagram.com/all_living_beings/\"><img src=\"../static/img/common/logo_instagram.jpg\" alt=\"logo instagram\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://www.deviantart.com/archiwyzard/\"><img src=\"../static/img/common/logo_deviantart.jpeg\" alt=\"logo deviantart\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://pixabay.com/users/sinason-14315822/\"><img src=\"../static/img/common/logo_pixabay.jpg\" alt=\"logo pixabay\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                <center></p>\n")
    foFILE_sheet.write("            </div>\n")
    foFILE_sheet.write("        </div>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("        <div class=\"content pure-u-1 pure-u-md-3-4\">\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <p><a href=\""+pageURL+"\" target=\"_blank\"><span style=\"font-weight: 400;\">Lien vers la photo sur DEVIANTART (link of the picture on DEVIANTART)</span></a></p>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <div class=\"photo-box pure-u-1 pure-u-md-1-2 pure-u-lg-1-2\">\n")
    foFILE_sheet.write("                <img width=100% height=100% src=\""+link+"\" alt=\""+alt+"\">\n")
    foFILE_sheet.write("                </div>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("        <div> <!-- div footer -->\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                    <div class=\"footer\">\n")
    foFILE_sheet.write("                        <p>Copyright &copy; Alexandre Proux </p>\n")
    foFILE_sheet.write("                    </div>\n")
    foFILE_sheet.write("            </div>\n")
    foFILE_sheet.write("        </div>\n")
    foFILE_sheet.write("    </div>\n")
    foFILE_sheet.write("</body>\n")
    foFILE_sheet.write("</html>\n")
    foFILE_sheet.close()

def createPic(imgList, templatePath, pagesList, imagePerPage):

    # create pages buttons before gallry 
    for pagesFiles in range(len(pagesList)):
        pagesList[pagesFiles]["foFILE"].write("\n")
        pagesList[pagesFiles]["foFILE"].write("    <p>Pages: \n")
        for pagesFilesWrite in range(len(pagesList)):
            pagesList[pagesFiles]["foFILE"].write("    <a href=\"/"+pagesList[pagesFilesWrite]["filename"]+"\" class=\"buttonPage\">"+str(pagesFilesWrite+1)+"</a>\n")
        pagesList[pagesFiles]["foFILE"].write("    </p>\n")
    
    borderCount = 0
    currentIMG = 0
    for deviation in imgList :
        if (((currentIMG%imagePerPage)==0) and (currentIMG != 0)):
            borderCount +=1
        pagesList[borderCount]["foFILE"].write("     <input class=\"gallery__select\"  type=\"radio\" name=\"autogenerated\" id=\""+str(currentIMG % imagePerPage)+"\"/>\n")
        currentIMG +=1
            
    for pagesFiles in range(len(pagesList)):
        pagesList[pagesFiles]["foFILE"].write("\n")
        pagesList[pagesFiles]["foFILE"].write("\n")
        pagesList[pagesFiles]["foFILE"].write("    <div class=\"gallery\">\n")
    
    borderCount = 0
    currentIMG = 0
    for deviation in imgList :
        link = format(deviation.content.get("src"))
        pageURL = format(deviation.url)
        alt = format(deviation.title)+" drawing deviantart archiwyzard"
        name = pageURL
        name = re.sub(r'(.*)?\/',"", name)
        if (((currentIMG%imagePerPage)==0) and (currentIMG != 0)):
            borderCount +=1
        pagesList[borderCount]["foFILE"].write("         <label class=\"gallery__item\" for=\""+str(currentIMG % imagePerPage)+"\">\n")
        pagesList[borderCount]["foFILE"].write("             <a href=\"/sheet-"+str(name)+"\" target=\"_blank\">\n")
        pagesList[borderCount]["foFILE"].write("             <img class=\"cover\" height=100% width=100% min-height=\"50px\" src=\""+link+"\" alt=\""+alt+"\"></a>\n")
        pagesList[borderCount]["foFILE"].write("         </label>\n")
        currentIMG +=1
            
        #### Generate file HTML for picture
        autoHTML(name, link, alt, templatePath, pageURL)
        
    for pagesFiles in range(len(pagesList)):
        pagesList[pagesFiles]["foFILE"].write("    </div> <!-- End div classe gallery -->\n")
        
    # create pages buttons after gallry 
    for pagesFiles in range(len(pagesList)):
        pagesList[pagesFiles]["foFILE"].write("\n")
        pagesList[pagesFiles]["foFILE"].write("    <p>Pages: \n")
        for pagesFilesWrite in range(len(pagesList)):
            pagesList[pagesFiles]["foFILE"].write("    <a href=\"/"+pagesList[pagesFilesWrite]["filename"]+"\" class=\"buttonPage\">"+str(pagesFilesWrite+1)+"</a>\n")
        pagesList[pagesFiles]["foFILE"].write("    </p>\n")

def gene_pic_gallery():
    ######################################
    ### Get IMG
    ######################################
    #https://github.com/neighbordog/deviantart/blob/master/deviantart/deviation.py

    #create an API object with your client credentials
    da = deviantart.Api("13119", "b363cdd42cd62852b84c93ad4eb82b05")

    #define defaults
    deviations = []

    #the name of the user we want to fetch deviations from
    username = "archiwyzard"

    offset = 0
    has_more = True

    #while there are more deviations to fetch
    while has_more:

        try:

            #fetch deviations from user
            fetched_deviations = da.get_gallery_folder(
                username=username,
                offset=offset,
                mode="newest",
            )
                
            #add fetched deviations to stack
            deviations += fetched_deviations['results']

            #update offset
            offset = fetched_deviations['next_offset']

            #check if there are any deviations left that we can fetch (if yes => repeat)
            has_more = fetched_deviations['has_more']

        except deviantart.api.DeviantartError as e:
            #catch and print API exception and stop loop
            print (e)
            has_more = False

    #print (deviations)
    total = len(deviations)
    print ("DEVIANTART: total deviations : ",total)
    
    imagePerPage = 24
    pagesHtml = round((total/imagePerPage)+0.5)

    ######################################
    ### Create paths 
    ######################################
    result = os.getcwd()

    templatePath = result+"/templates"
    cssPath = result+"/static/css/layouts"

    ######################################
    ### HTML part 
    ######################################
    foFILEout = open (templatePath+"/galerie_peinture.html", "r");
    
    ##### ALL
    pagesList = []
    dictionnary = {}
    dictionnary["filename"] = "galerie_peinture"
    dictionnary["htmlfile"] = "htmlfile"
    dictionnary["foFILE"] = open (templatePath+"/htmlfile.txt", "w");
    pagesList.append(dictionnary)
    for pagesFiles in range(1, pagesHtml):
        dictionnary = {}
        dictionnary["filename"] = "galerie_peinture-page"+str(pagesFiles)
        dictionnary["htmlfile"] = "htmlfile-page"+str(pagesFiles)
        dictionnary["foFILE"] = open (templatePath+"/"+dictionnary["htmlfile"]+".txt", "w");
        pagesList.append(dictionnary)    
    
    print ("PAGES all : "+str(pagesHtml))
    
    foFILE = open (templatePath+"/htmlfile.txt", "w");
    copy = 1
    for line in foFILEout:
        if (copy == 1):
            for pagesFiles in range(0, pagesHtml):
                pagesList[pagesFiles]["foFILE"].write(line)
       
        if (re.search("end autogenerated", line)):
            copy = 1
            for pagesFiles in range(0, pagesHtml):
                pagesList[pagesFiles]["foFILE"].write(line)
       
        if (re.search("start autogenerated", line)):
            copy = 0    
            createPic(deviations, templatePath, pagesList, imagePerPage)
      
    for pagesFiles in range(0, pagesHtml):
        os.system("mv "+templatePath+"/"+pagesList[pagesFiles]["htmlfile"]+".txt "+templatePath+"/"+pagesList[pagesFiles]["filename"]+".html")
        
    for pagesFiles in range(0, pagesHtml):
        pagesList[pagesFiles]["foFILE"].close()

    ######################################
    ### auto generate CSS
    ######################################
    foFILE = open (cssPath+"/gallery_paintings1.css", "w");
    foFILE.write("* {\n")
    foFILE.write("  box-sizing: border-box;\n")
    foFILE.write("  -webkit-animation: fadeIn 0.5s;\n")
    foFILE.write("          animation: fadeIn 0.5s;\n")
    foFILE.write("}\n")
    foFILE.write("\n")
    foFILE.write(".cover {object-fit: cover;}\n")
    foFILE.write("\n")
    foFILE.write(".gallery {\n")
    foFILE.write("    display: grid;\n")
    foFILE.write("    justify-content: center;\n")
    foFILE.write("    grid-template-columns: repeat(4, 300px);\n")
    foFILE.write("    grid-gap: 20px;\n")
    foFILE.write("    grid-template-rows: repeat("+str(round(imagePerPage/4))+", 300px);\n")
    foFILE.write("}\n")
    foFILE.write("\n")
    foFILE.write("@media (max-width: 768px) {\n")
    foFILE.write("  .gallery {\n")
    foFILE.write("    grid-gap: 10px;\n")
    foFILE.write("    grid-template-columns: repeat(auto-fit, 100px);\n")
    foFILE.write("    grid-template-rows: repeat(auto-fit, 100px);\n")
    foFILE.write("  }\n")
    foFILE.write("}\n")
    foFILE.write("\n")
    foFILE.write(".gallery__item {\n")
    foFILE.write("  cursor: pointer;\n")
    foFILE.write("  border-radius: 5px;\n")
    foFILE.write("  grid-row: span 1;\n")
    foFILE.write("  grid-column: span 1;\n")
    foFILE.write("  transition: -webkit-transform 0.1s ease-in-out;\n")
    foFILE.write("  transition: transform 0.1s ease-in-out;\n")
    foFILE.write("  transition: transform 0.1s ease-in-out, -webkit-transform 0.1s ease-in-out;\n")
    foFILE.write("}\n")
    foFILE.write(".gallery__item:hover {\n")
    foFILE.write("  -webkit-transform: scale(1.1) rotate(5deg);\n")
    foFILE.write("          transform: scale(1.1) rotate(5deg);\n")
    foFILE.write("}\n")
    foFILE.write("\n")
    foFILE.write(".gallery__select {\n")
    foFILE.write("  display: none;\n")
    foFILE.write("}\n")

    for nbr in range(imagePerPage):
        foFILE.write(".gallery__select:nth-of-type("+str(nbr)+"):checked ~ .gallery .gallery__item:nth-of-type("+str(nbr)+") {\n")
        foFILE.write("  cursor: default;\n")
        foFILE.write("  display: grid;\n")
        foFILE.write("  align-items: center;\n")
        foFILE.write("  grid-row: 1/-1;\n")
        foFILE.write("  grid-column: 3;\n")
        foFILE.write("}\n")
        foFILE.write(".gallery__select:nth-of-type("+str(nbr)+"):checked ~ .gallery .gallery__item:nth-of-type("+str(nbr)+"):hover {\n")
        foFILE.write("  -webkit-transform: none;\n")
        foFILE.write("          transform: none;\n")
        foFILE.write("}\n")
        foFILE.write("@media (max-width: 768px) {\n")
        foFILE.write("  .gallery__select:nth-of-type(1):checked ~ .gallery .gallery__item:nth-of-type(1) {\n")
        foFILE.write("    grid-row: 1/-3;\n")
        foFILE.write("    grid-column: 1/-1;\n")
        foFILE.write("  }\n")
        foFILE.write("}\n")
    
    
    foFILE.write("@-webkit-keyframes fadeIn {\n")
    foFILE.write("  from {\n")
    foFILE.write("    opacity: 0;\n")
    foFILE.write("  }\n")
    foFILE.write("  to {\n")
    foFILE.write("    opacity: 1;\n")
    foFILE.write("  }\n")
    foFILE.write("}\n")
    foFILE.write("@keyframes fadeIn {\n")
    foFILE.write("  from {\n")
    foFILE.write("    opacity: 0;\n")
    foFILE.write("  }\n")
    foFILE.write("  to {\n")
    foFILE.write("    opacity: 1;\n")
    foFILE.write("  }\n")
    foFILE.write("}\n")
    foFILE.close();

