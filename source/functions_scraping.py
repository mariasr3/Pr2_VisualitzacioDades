# Title: Functions to scrape Teatre de Barcelona web page
# Date 13/11/2023
# Authors: Maria Sopena & Joana Llauradó
# Description: Functions used to obtain the information stored in different elements in Teatre de Barcelona web page 

from bs4 import BeautifulSoup
import requests
from IPython.display import SVG, display

def get_url(ordenar_per, vull_veure, data,preu_minim, preu_maxim, lloc):
    url = 'https://www.teatrebarcelona.com/cartellera-teatre-barcelona/pagina/1/f/list/%s/%s/0/%s/%s:%s/%s/all/0/0/0' \
%(ordenar_per, vull_veure, data,preu_minim, preu_maxim,lloc)
    
    return(url)

def get_title(bs4_object):
    
    if bs4_object.find("div", class_="e"):
        title_teatre = bs4_object.find('a', {'class': 'tooltip'})['data-title']
        title_split = title_teatre.split(" → ")
        if len(title_split) == 2:
            title = title_split[0]
            teatre = title_split[1]
        else:
            title = title_split[0]
            teatre = "No especificat"

    else:
        # If "e" does not exist, find the <div> element with class "ts" and extract the text
        title_div = fbs4_object.find('div', class_='ts')
        title_teatre = title_div.get_text(strip=True)
        title_split = title_teatre.split(" → ")
        if len(title_split) == 2:
            title = title_split[0]
            teatre = title_split[1]
        else:
            title = title_split[0]
            teatre = "No especificat"
    return(title, teatre)
    
    
    
def get_date(bs4_object):

    tx_div = bs4_object.find('div', class_='tx')
    d_div = tx_div.find('div', class_='d')
    d_div_span = d_div.find('span', class_='el-mobile')
    
    if d_div_span: 
        dates_span = d_div_span.get_text() 
        date_parts = dates_span.split("Fins:")  #borrem fins: i obtenim llista

        if len(date_parts) == 2 :
            des_de_date = date_parts[0].replace("Des de:", "").strip()
            fins_date = date_parts[1].strip()

        elif len(date_parts) == 1 :
            des_de_date = date_parts[0].replace("El", "").strip()
            fins_date = des_de_date
    else:
        des_de_date = "No especificat"
        fins_date = "No especificat"
    return(des_de_date, fins_date)


def get_price(bs4_object):
    
    price = None 
    
    price_dis = bs4_object.find('div', class_="p")
    price_div = bs4_object.find('div', class_="price")
    next_div = bs4_object.find('div', class_ ="next")

    if price_dis != None:
        actual_price = price_dis.find('span', class_="price").text
        discount = price_dis.find('span', class_="sale").text
        old_price = price_dis.find('div', class_="o").text.strip()
        price = actual_price
        #print("Preu: ", actual_price, discount, old_price)

    if price_div != None:
        price_span = price_div.find('span')
        price = price_span.get_text(strip=True)
        #print("Preu: ", price)

    if next_div != None:
        not_price = next_div.text.strip() # You can use .text to extract the text
        price = not_price   
    return(price)

def get_rate(bs4_object):
    palmas_div = bs4_object.find('div', class_='palmas')

    if palmas_div != None:
        # Find the <div> element with class "rate" within the "palmas" div
        rate_div = palmas_div.find('div', class_='rate')
        # Extract the rate percentage from the "rate" div
        rate_percentage = rate_div['style']
        clean_rate = rate_percentage.replace("width: ", "")

    if palmas_div == None:
        clean_rate = "0%"
    return(clean_rate)
        
def get_sinopsis(bs4_object):
    sinopsis_div = bs4_object.find('div', class_='synopsis el-desktop')
    presentation_div = bs4_object.find('div', class_='presentation')

    if sinopsis_div:
        p_elements = sinopsis_div.find_all('p')
        if len(p_elements) > 0:
            sinopsis = ' '.join(p.get_text() for p in p_elements)
        else:
            sinopsis = "Sinopsis not found"
    elif presentation_div:
        sinopsis = presentation_div.get_text()
    else:
        sinopsis = "Sinopsis not found"
    
    return(sinopsis)

def get_additional_info(bs4_object):
    
    durada, idioma,edat = None, None, None
    
    info_div = bs4_object.find('div', class_='info')
    items = info_div.find_all('div', class_='item')
    
    for item in items:
        t_element = item.find('div', class_='t')
        if t_element:
            text = t_element.get_text(strip=True)
            if "Durada:" in text:
                durada = text.replace("Durada:", "").strip()
            if "Idioma:" in text:
                idioma = text.replace("Idioma:", "").strip()
            if "Edat:" in text:
                edat = text.replace("Edat:", "").strip()
        else:
            durada = "No especificada"
            idioma = "No especificat"
            edat = "No especificada"
    return(durada, idioma, edat)








