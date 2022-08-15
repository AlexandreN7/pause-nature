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
    foFILE_sheet = open (templatePath+"/sheet-paintings-"+name+".html", "w")
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
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/reviews\">Articles : randonnées et art</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/gallery_paintings\">Dessins et aquarelles</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/gallery_paintings\">Photographie</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/about\">A-propos</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                    </ul>\n")
    foFILE_sheet.write("                </nav>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <p><center>\n")
    foFILE_sheet.write("                    <a href=\"https://www.instagram.com/archiwyzard/\"><img src=\"../static/img/common/logo_instagram.jpg\" alt=\"logo instagram\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://www.instagram.com/all_living_beings/\"><img src=\"../static/img/common/logo_instagram.jpg\" alt=\"logo instagram\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://www.deviantart.com/archiwyzard/\"><img src=\"../static/img/common/logo_deviantart.jpeg\" alt=\"logo deviantart\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://pixabay.com/users/sinason-14315822/\"><img src=\"../static/img/common/logo_pixabay.jpg\" alt=\"logo pixabay\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://www.deviantart.com/sinason/\"><img src=\"../static/img/common/logo_deviantart.jpeg\" alt=\"logo deviantart\" height=\"30px\" width=\"30px\" /></a>\n")
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
    
    foFILE_sheet.write("                <script async src=\"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>\n")
    foFILE_sheet.write("                <ins class=\"adsbygoogle\"\n")
    foFILE_sheet.write("                style=\"display:block; text-align:center;\"\n")
    foFILE_sheet.write("                data-ad-layout=\"in-article\"\n")
    foFILE_sheet.write("                data-ad-format=\"fluid\"\n")
    foFILE_sheet.write("                data-ad-client=\"ca-pub-4353004932795007\"\n")
    foFILE_sheet.write("                data-ad-slot=\"5273903670\"></ins>\n")
    foFILE_sheet.write("                <script>\n")
    foFILE_sheet.write("                (adsbygoogle = window.adsbygoogle || []).push({});\n")
    foFILE_sheet.write("                </script>\n")
    
    foFILE_sheet.write("\n")
    foFILE_sheet.write("        <div> <!-- div footer -->\n")
    foFILE_sheet.write("                    <div class=\"footer\">\n")
    foFILE_sheet.write("                        <p>Copyright &copy; Alexandre Proux </p>\n")
    foFILE_sheet.write("                    </div>\n")
    foFILE_sheet.write("            </div>\n")
    foFILE_sheet.write("        </div>\n")
    foFILE_sheet.write("    </div>\n")
    foFILE_sheet.write("</body>\n")
    foFILE_sheet.write("</html>\n")
    foFILE_sheet.close()

def createPic(imgList, templatePath, pagesList, imagePerPage, imagePerCol):

    # create pages buttons before gallry 
    for pagesFiles in range(len(pagesList)):
        pagesList[pagesFiles]["foFILE"].write("\n")
        pagesList[pagesFiles]["foFILE"].write("    <p>Pages: \n")
        for pagesFilesWrite in range(len(pagesList)):
            pagesList[pagesFiles]["foFILE"].write("    <a href=\"/"+pagesList[pagesFilesWrite]["filename"]+"\" class=\"buttonPage\">"+str(pagesFilesWrite+1)+"</a>\n")
        pagesList[pagesFiles]["foFILE"].write("    </p>\n")
    
    borderCount = 0
    currentIMG = 0
            
    for pagesFiles in range(len(pagesList)):
        pagesList[pagesFiles]["foFILE"].write("\n")
        pagesList[pagesFiles]["foFILE"].write("\n")
        pagesList[pagesFiles]["foFILE"].write("<link href=\"https://fonts.googleapis.com/css2?family=Raleway:wght@400&display=swap\" rel=\"stylesheet\">\n");
        pagesList[pagesFiles]["foFILE"].write("    <div class=\"gallery\">\n")
    
    borderCount = 0
    currentIMG = 0
    currentIMGCol = 0
    for deviation in imgList :
        
        #print (deviation.content)
        #print (deviation.thumbs)
        
        linkBIG = format(deviation.content.get("src")) # big big image 
        link = format(deviation.thumbs[2].get("src"))
        pageURL = format(deviation.url)
        alt = format(deviation.title)+" drawing deviantart archiwyzard"
        name = pageURL
        name = re.sub(r'(.*)?\/',"", name)
        if ((currentIMG%imagePerPage)==0):
            if (currentIMG != 0):
                pagesList[borderCount]["foFILE"].write("\t\t</div>\n\n") # Close previous
                borderCount +=1
            
            # Open new div section
            pagesList[borderCount]["foFILE"].write("\t\t<div class=\"gallery__column\">\n")
            currentIMGCol = 0

        elif (currentIMGCol>=imagePerCol):
            pagesList[borderCount]["foFILE"].write("\t\t</div>\n\n") # Close previous
            # Open new
            pagesList[borderCount]["foFILE"].write("\t\t<div class=\"gallery__column\">\n")
            currentIMGCol = 0
            
        pagesList[borderCount]["foFILE"].write("\t\t\t<a href=\"/sheet-paintings-"+str(name)+"\" target=\"_blank\" class=\"gallery__link\">\n")
        pagesList[borderCount]["foFILE"].write("\t\t\t\t<figure class=\"gallery__thumb\">\n")
        pagesList[borderCount]["foFILE"].write("\t\t\t\t\t<img src=\""+link+"\" alt=\""+alt+"\" class=\"gallery__image\">\n")
        pagesList[borderCount]["foFILE"].write("\t\t\t\t\t<figcaption class=\"gallery__caption\">"+alt+"<figcaption>\n")
        pagesList[borderCount]["foFILE"].write("\t\t\t\t</figure>\n")
        pagesList[borderCount]["foFILE"].write("\t\t\t</a>\n")
        currentIMG +=1
        currentIMGCol += 1

        #### Generate file HTML for picture
        autoHTML(name, linkBIG, alt, templatePath, pageURL)
        
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
    print ("DEVIANTART ARCHIW: total deviations : ",total)
    
    imagePerPage = 24
    imagePerCol = int(imagePerPage/4)
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
    foFILEout = open (templatePath+"/gallery_paintings.html", "r");
    
    ##### ALL
    pagesList = []
    dictionnary = {}
    dictionnary["filename"] = "gallery_paintings"
    dictionnary["htmlfile"] = "htmlfile"
    dictionnary["foFILE"] = open (templatePath+"/htmlfile.txt", "w");
    pagesList.append(dictionnary)
    for pagesFiles in range(1, pagesHtml):
        dictionnary = {}
        dictionnary["filename"] = "gallery_paintings-page"+str(pagesFiles)
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
            createPic(deviations, templatePath, pagesList, imagePerPage, imagePerCol)
      
    for pagesFiles in range(0, pagesHtml):
        os.system("mv "+templatePath+"/"+pagesList[pagesFiles]["htmlfile"]+".txt "+templatePath+"/"+pagesList[pagesFiles]["filename"]+".html")
        
    for pagesFiles in range(0, pagesHtml):
        pagesList[pagesFiles]["foFILE"].close()

