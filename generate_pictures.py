#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
import re 
from pixabay import Image, Video

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
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/galerie_pictures\">Pictures</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                        <li class=\"nav-item\">\n")
    foFILE_sheet.write("                            <a class=\"pure-button\" href=\"/about\">About</a>\n")
    foFILE_sheet.write("                        </li>\n")
    foFILE_sheet.write("                    </ul>\n")
    foFILE_sheet.write("                </nav>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <p><center>\n")
    foFILE_sheet.write("                    <a href=\"https://www.instagram.com/archiwyzard/\"><img src=\"../static/img/common/logo_instagram.jpg\" alt=\"logo instagram\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://www.deviantart.com/archiwyzard/\"><img src=\"../static/img/common/logo_deviantart.jpeg\" alt=\"logo deviantart\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                    <a href=\"https://pixabay.com/users/sinason-14315822/\"><img src=\"../static/img/common/logo_pixabay.jpg\" alt=\"logo pixabay\" height=\"30px\" width=\"30px\" /></a>\n")
    foFILE_sheet.write("                <center></p>\n")
    foFILE_sheet.write("            </div>\n")
    foFILE_sheet.write("        </div>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("        <div class=\"content pure-u-1 pure-u-md-3-4\">\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <p><a href=\""+pageURL+"\" target=\"_blank\"><span style=\"font-weight: 400;\">Lien vers la photo sur PIXABAY (link of the picture on PIXABAY)</span></a></p>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("                <div class=\"photo-box pure-u-1 pure-u-md-1-2 pure-u-lg-1-2\">\n")
    foFILE_sheet.write("                <img width=100% height=100% src=\""+link+"\" alt=\""+alt+"\">\n")
    foFILE_sheet.write("                </div>\n")
    foFILE_sheet.write("\n")
    foFILE_sheet.write("            <div> <!-- div footer -->\n")
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
    for elements in range(len(imgList)):
        imageData = imgList[elements]
        totalhits = imageData['totalHits']
        
        # create pages buttons before gallry 
        for pagesFiles in range(len(pagesList)):
            pagesList[pagesFiles]["foFILE"].write("\n")
            pagesList[pagesFiles]["foFILE"].write("    <p>Pages: \n")
            for pagesFilesWrite in range(len(pagesList)):
                pagesList[pagesFiles]["foFILE"].write("    <a href=\"/"+pagesList[pagesFilesWrite]["filename"]+"\" class=\"buttonPage\">"+str(pagesFilesWrite+1)+"</a>\n")
            pagesList[pagesFiles]["foFILE"].write("    </p>\n")
        
        borderCount = 0
        for imageNb in range(totalhits) :
            currentIMG = imageNb+elements*200 # PIXABAY PAGE contains 200 pictures
            if (((currentIMG%imagePerPage)==0) and (currentIMG != 0)):
                borderCount +=1
            pagesList[borderCount]["foFILE"].write("     <input class=\"gallery__select\"  type=\"radio\" name=\"autogenerated\" id=\""+str(currentIMG % imagePerPage)+"\"/>\n")
                
        for pagesFiles in range(len(pagesList)):
            pagesList[pagesFiles]["foFILE"].write("\n")
            pagesList[pagesFiles]["foFILE"].write("\n")
            pagesList[pagesFiles]["foFILE"].write("    <div class=\"gallery\">\n")
        
        borderCount = 0
        for imageNb in range(totalhits) :
            currentIMG = imageNb+elements*200 # PIXABAY PAGE contains 200 pictures
            alt = imageData['hits'][imageNb]['tags']
            link = imageData['hits'][imageNb]['previewURL']
            link = link.replace("_150.jpg","_960_720.jpg")
            name = link
            name = name.replace("_960_720.jpg","")
            name = re.sub(r'(.*)?\/', '', name)
            if (((currentIMG%imagePerPage)==0) and (currentIMG != 0)):
                borderCount +=1
            pagesList[borderCount]["foFILE"].write("         <label class=\"gallery__item\" for=\""+str(currentIMG % imagePerPage)+"\">\n")
            pagesList[borderCount]["foFILE"].write("             <a href=\"/sheet-"+str(name)+"\" target=\"_blank\">\n")
            pagesList[borderCount]["foFILE"].write("             <img class=\"cover\" height=100% width=100% min-height=\"50px\" src=\""+link+"\" alt=\""+alt+"\"></a>\n")
            pagesList[borderCount]["foFILE"].write("         </label>\n")
                
            #### Generate file HTML for picture
            autoHTML(name, link, alt, templatePath, imageData['hits'][imageNb]['pageURL'])
            
        for pagesFiles in range(len(pagesList)):
            pagesList[pagesFiles]["foFILE"].write("    </div> <!-- End div classe gallery -->\n")
            
        # create pages buttons after gallry 
        for pagesFiles in range(len(pagesList)):
            pagesList[pagesFiles]["foFILE"].write("\n")
            pagesList[pagesFiles]["foFILE"].write("    <p>Pages: \n")
            for pagesFilesWrite in range(len(pagesList)):
                pagesList[pagesFiles]["foFILE"].write("    <a href=\"/"+pagesList[pagesFilesWrite]["filename"]+"\" class=\"buttonPage\">"+str(pagesFilesWrite+1)+"</a>\n")
            pagesList[pagesFiles]["foFILE"].write("    </p>\n")
            
            
def createPicSorted(imgList, templatePath, pagesList, imagePerPage, pagesReal, typeOfSort, regex, notRegex):
    currentIMG = 0
    for elements in range(len(imgList)):
        imageData = imgList[elements]
        totalhits = imageData['totalHits']
        
        # create pages buttons before gallry 
        for pagesFiles in range(len(pagesList)):
            if pagesFiles < pagesReal:
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("\n")
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("    <p>Pages: \n")
                for pagesFilesWrite in range(len(pagesList)):
                    if pagesFilesWrite < pagesReal:
                        pagesList[pagesFiles][typeOfSort]["foFILE"].write("    <a href=\"/"+pagesList[pagesFilesWrite][typeOfSort]["filename"]+"\" class=\"buttonPage\">"+str(pagesFilesWrite+1)+"</a>\n")
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("    </p>\n")
        
        borderCount = 0
        currentIMGint = currentIMG
        for imageNb in range(totalhits) :
            alt = imageData['hits'][imageNb]['tags']
            concate = alt+" "+imageData['hits'][imageNb]['pageURL']
            if ((re.search(regex, concate)) and (not re.search(notRegex,concate))):
                if (((currentIMGint%imagePerPage)==0) and (currentIMGint != 0)):
                    borderCount +=1
                pagesList[borderCount][typeOfSort]["foFILE"].write("     <input class=\"gallery__select\"  type=\"radio\" name=\"autogenerated\" id=\""+str(currentIMGint % imagePerPage)+"\"/>\n")
                currentIMGint +=1
                
        for pagesFiles in range(len(pagesList)):
            if pagesFiles < pagesReal:
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("\n")
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("\n")
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("    <div class=\"gallery\">\n")
        
        borderCount = 0
        currentIMGint = currentIMG
        for imageNb in range(totalhits) :
            alt = imageData['hits'][imageNb]['tags']
            link = imageData['hits'][imageNb]['previewURL']
            link = link.replace("_150.jpg","_960_720.jpg")
            name = link
            name = name.replace("_960_720.jpg","")
            name = re.sub(r'(.*)?\/', '', name)
            concate = alt+" "+imageData['hits'][imageNb]['pageURL']
            if ((re.search(regex, concate)) and (not re.search(notRegex,concate))):
                if (((currentIMGint%imagePerPage)==0) and (currentIMGint != 0)):
                    borderCount +=1
                pagesList[borderCount][typeOfSort]["foFILE"].write("         <label class=\"gallery__item\" for=\""+str(currentIMGint % imagePerPage)+"\">\n")
                pagesList[borderCount][typeOfSort]["foFILE"].write("             <a href=\"/sheet-"+str(name)+"\" target=\"_blank\">\n")
                pagesList[borderCount][typeOfSort]["foFILE"].write("             <img class=\"cover\" height=100% width=100% min-height=\"50px\" src=\""+link+"\" alt=\""+alt+"\"></a>\n")
                pagesList[borderCount][typeOfSort]["foFILE"].write("         </label>\n")
                currentIMGint +=1
                
        for pagesFiles in range(len(pagesList)):
            if pagesFiles < pagesReal:
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("    </div> <!-- End div classe gallery -->\n")
            
        # create pages buttons after gallry 
        for pagesFiles in range(len(pagesList)):
            if pagesFiles < pagesReal:
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("\n")
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("    <p>Pages: \n")
                for pagesFilesWrite in range(len(pagesList)):
                    if pagesFilesWrite < pagesReal:
                        pagesList[pagesFiles][typeOfSort]["foFILE"].write("    <a href=\"/"+pagesList[pagesFilesWrite][typeOfSort]["filename"]+"\" class=\"buttonPage\">"+str(pagesFilesWrite+1)+"</a>\n")
                pagesList[pagesFiles][typeOfSort]["foFILE"].write("    </p>\n")
            
        currentIMG = currentIMGint

def gene_pic_gallery():
    ######################################
    ### Get IMG
    ######################################
    # https://github.com/momozor/python-pixabay.git
    API_KEY = '14315822-1ee9a66d3b41ea088716f70d1'

    # image operations
    image = Image(API_KEY)
    imgList = []

    # custom image search
    total = 1000000
    totalhits = 0
    pageNb = 0
    while (totalhits < total):
        ims = image.search(q='user:sinason',
                image_type='photo',
                order='latest',
                page=(pageNb+1),
                per_page=200)
        total = ims['total']
        totalhits = ims['totalHits'] + totalhits
        print("PIXABAY: nombre d'images : ",total)
        print("PIXABAY: nombre de hits : ",totalhits)
        imgList.append(ims)
        pageNb+=1
    
    #print (ims)
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
    foFILEout = open (templatePath+"/galerie_pictures.html", "r");

    ##### ALL
    pagesList = []
    dictionnary = {}
    dictionnary["filename"] = "galerie_pictures"
    dictionnary["htmlfile"] = "htmlfile"
    dictionnary["foFILE"] = open (templatePath+"/htmlfile.txt", "w");
    pagesList.append(dictionnary)
    for pagesFiles in range(1, pagesHtml):
        dictionnary = {}
        dictionnary["filename"] = "galerie_pictures-page"+str(pagesFiles)
        dictionnary["htmlfile"] = "htmlfile-page"+str(pagesFiles)
        dictionnary["foFILE"] = open (templatePath+"/"+dictionnary["htmlfile"]+".txt", "w");
        pagesList.append(dictionnary)
        
    ##### SORTED 
    tri = [["insects", 0, "insect|dragonfly|butterfly|mantis|ladybug|bee|chafer|caterpillar", "emptyNothing"], 
           ["living", 0, "insect|dragonfly|butterfly|mantis|ladybug|bee|chafer|caterpillar|animal|bird|cat|frog|reptile|snake", "emptyNothing"], 
           ["giverny", 0, "giverny|monet|nympheas", "emptyNothing"],
           ["mountain", 0, "mountain|alps", "emptyNothing"], 
           ["flower", 0, "flower|blossom|garden|rose", "insect|dragonfly|butterfly|mantis|ladybug|bee|chafer|caterpillar|animal|bird|cat|frog|reptile|snake"]]
  
    print ("PAGES all : "+str(pagesHtml))
    for element in range(len(tri)):
        tri[element][1] = analyzeImgNbrToGetPages(imgList, imagePerPage, tri[element][2], tri[element][3])
        print ("PAGES "+tri[element][0]+" : "+str(tri[element][1]))
    
    pagesListTri = []
    for pagesFiles in range(pagesHtml):
        dictionnary = {}
        for x in tri:
            if (pagesFiles < x[1]):
                htmlFileName = "htmlfile"+str(x[0])+"-page"+str(pagesFiles)
                dictionnary[x[0]] = {"filename": "galerie_pictures-"+str(x[0])+"-page"+str(pagesFiles),
                                     "htmlfile": htmlFileName,
                                     "foFILE": open (templatePath+"/"+htmlFileName+".txt", "w") } 
            else:
                dictionnary[x[0]] = "None"
        if (dictionnary):
            pagesListTri.append(dictionnary)
        
    # START GENERATION
    copy = 1
    for line in foFILEout:
        if (copy == 1):
            for pagesFiles in range(0, pagesHtml):
                pagesList[pagesFiles]["foFILE"].write(line)
                for x in tri:
                    if (pagesListTri[pagesFiles][x[0]] != "None"):
                        pagesListTri[pagesFiles][x[0]]["foFILE"].write(line)
                
        if (re.search("end autogenerated", line)):
            copy = 1
            for pagesFiles in range(0, pagesHtml):
                pagesList[pagesFiles]["foFILE"].write(line)
                for x in tri:
                    if (pagesListTri[pagesFiles][x[0]] != "None"):
                        pagesListTri[pagesFiles][x[0]]["foFILE"].write(line)      
       
        if (re.search("start autogenerated", line)):
            copy = 0    
            createPic(imgList, templatePath, pagesList, imagePerPage)
            for element in range(len(tri)):
                createPicSorted(imgList, templatePath, pagesListTri, imagePerPage, tri[element][1], tri[element][0], tri[element][2], tri[element][3])
            
      
    for pagesFiles in range(0, pagesHtml):
        os.system("mv "+templatePath+"/"+pagesList[pagesFiles]["htmlfile"]+".txt "+templatePath+"/"+pagesList[pagesFiles]["filename"]+".html")
        for x in tri:
            if pagesFiles < x[1]:
                os.system("mv "+templatePath+"/"+pagesListTri[pagesFiles][x[0]]["htmlfile"]+".txt "+templatePath+"/"+pagesListTri[pagesFiles][x[0]]["filename"]+".html")
    
    for pagesFiles in range(0, pagesHtml):
        pagesList[pagesFiles]["foFILE"].close()
        for x in tri:
            if pagesFiles < x[1]:
                pagesListTri[pagesFiles][x[0]]["foFILE"].close()
    
    ######################################
    ### auto generate CSS
    ######################################
    foFILE = open (cssPath+"/gallery_picture1.css", "w");
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
        foFILE.write("  .gallery__select:nth-of-type("+str(nbr)+"):checked ~ .gallery .gallery__item:nth-of-type("+str(nbr)+") {\n")
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


def analyzeImgNbrToGetPages(imgList, imgPerPage, regex, notRegex):
    currentIMG = 0
    for elements in range(len(imgList)):
        imageData = imgList[elements]
        totalhits = imageData['totalHits']
    
        for imageNb in range(totalhits) :
            alt = imageData['hits'][imageNb]['tags']
            concate = alt+" "+imageData['hits'][imageNb]['pageURL']
            if ((re.search(regex, concate)) and (not re.search(notRegex,concate))):
                currentIMG +=1

    return round((currentIMG/imgPerPage)+0.5)
