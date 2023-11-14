# Title: Web scraping Teatre de Barcelona Web Page
# Date 13/11/2023
# Authors: Maria Sopena & Joana Llauradó
# Description: Perform and avdance search in Teatre de Barcelona and obtain the information applying web scraping.  

import csv 
import requests
from bs4 import BeautifulSoup
import pandas as pd
from functions_scraping import * 
#from parameters import filename
from parameters import *


def main(url, filename):
    
    # Create an empty list to store the scraped data
    all_data = []
    
    # Initialize a variable to track the current page number
    current_page = 1
    
    
    # Set the maximum number of pages to scrape
    max_pages = 5  # Change this to the number of pages you want to scrape (5 by default)
    
    while current_page <= max_pages:
        print("--------------------------------PAGE", current_page, "---------------------------------------")
        
        # Construct the URL for the current page
        page_url = f'{url}/pagina/{current_page}'
        
        # Send an HTTP GET request to the page
        response = requests.get(page_url)
        
        if response.status_code == 200:
            
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract "funcion-item-list" elements
            funcion_items = soup.find_all('div', class_='funcion-item-list')
        
            # Loop through each "funcion-item-list" and extract the desired information
            for funcion_item in funcion_items: # for each item in the funcion item we can extratc info 
                title, teatre = get_title(funcion_item)
                des_de_date, fins_date = get_date(funcion_item)
                preu = get_price(funcion_item)
                rating = get_rate(funcion_item)

                #LINK - more info per cada obra 
                inf_link = funcion_item.find('a', class_='inf')
                href = inf_link['href']

                individual_response = requests.get(href)
                individual_soup = BeautifulSoup(individual_response.text, 'html.parser')

                text_sinopsis = get_sinopsis(individual_soup)
                durada, idioma, edat = get_additional_info(individual_soup)
                 # Store the extracted data in a dictionary
                print(title)
                data = {
                    "Title": title,
                    "Nom Teatre": teatre, 
                    "Price": preu,
                    "Data d'inici": des_de_date,
                    "Data final": fins_date,
                    "Rating": rating,
                    "Sinopsis": text_sinopsis,
                    "Durada" : durada,
                    "Idioma": idioma,
                    "Edat": edat
                }

                # Append the data to the all_data list
                all_data.append(data)
            # Increment the current_page variable to move to the next page
            current_page += 1
        else:
            break  # Exit the loop in case of an error
    result = pd.DataFrame(all_data)
    # Save the DataFrame to a CSV file
    result.to_csv(filename, index=False)
    
# Call main 
if __name__ == "__main__":
    url = get_url(ordenar_per, vull_veure, data,preu_minim, preu_maxim, lloc)
    main(url, filename)
    
    