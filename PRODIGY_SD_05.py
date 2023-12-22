#Web Scraping 

#Create a program that extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.



#You are free to choose the website you scrape from.

import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_data(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product information
        product_list = []
        for product in soup.find_all('div', class_='product'):
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            rating = product.find('span', class_='product-rating').text.strip()

            product_data = {'Name': name, 'Price': price, 'Rating': rating}
            product_list.append(product_data)

        return product_list
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def save_to_csv(product_list, output_file='product_data.csv'):
    # Save product data to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()

        # Write the product data
        for product in product_list:
            writer.writerow(product)

if __name__ == "__main__":
    # Specify the URL of the e-commerce website you want to scrape
    target_url = input("Enter the url")

    # Scrape product data
    product_data = scrape_product_data(target_url)

    if product_data:
        # Save the data to a CSV file
        save_to_csv(product_data)
        print("Product data has been successfully scraped and saved to 'product_data.csv'.")
    else:
        print("Unable to scrape product data.")
