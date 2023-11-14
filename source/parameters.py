# Title: Parameters advanced search Teatre de Barcelona web page
# Date 13/11/2023
# Authors: Maria Sopena & Joana Llauradó
# Description: To perform an advanced search in the web page of Teatre de barcelona we can built up the url were such
# parameters are specified. For each parameters there are described the possible options. The user can choose such options
# and obtain the desired information. 


# ORDER BY (ordenar_per) -> Options: "popular", "rate"

# TYPE OF (vull_veure) -> Options: tot = 0 , cabaret = 11, circ = 14, dans = 4, escena hibrida 805, experiencies = 1082, humor = 9, infantil = 3, juvenil = 737, magia = 6, musica = 620, musicals = 8, opera, 5, sarsuela = 1895, teatre= 2

# PRICE (preu_mminim i preu_maxim) -> From 0 to 200

# DATES (data)
#data= 'all'  #qualsevol
#data = '2023-11-09' #avui
#data = '2023-11-11:2023-11-12'#proper cap de setmana
#data = '2023-11-11:2023-11-16'#propers 7 dies 
#data = '2023-11-09:2023-12-09'#propers 30 dies 
#data = '2023-11-10:2023-12-16'#random 

# PLACE (lloc) -> options: "Badalona", "Cornellà½20del%20Llobregat", "Figueres", "Girona", "Granollers"...etc.(see other options in web page)

# ADVANCED SEARCH PARAMETERS
ordenar_per = "popular" # order by most popular theatre plays
vull_veure = 2 # see theatre 
preu_minim = 0 # minimum price free
preu_maxim = 200  # maximum price 200€
data = '2023-11-13:2023-12-13'# propers 30 dies 
lloc = 'Barcelona'
filename = "web_scraping_teatre_barcelona_13112023.csv"

url = 'https://www.teatrebarcelona.com/cartellera-teatre-barcelona/pagina/1/f/list/%s/%s/0/%s/%s:%s/%s/all/0/0/0' \
%(ordenar_per, vull_veure, data,preu_minim, preu_maxim,lloc)

#print(url)