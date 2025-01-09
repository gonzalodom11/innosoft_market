#encoding:utf-8

from bs4 import BeautifulSoup
import urllib.request
import re
import os, ssl
import django
from .models import Category, Product

# lineas para evitar error SSL
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def populateDatabase():
    Category.objects.filter(name__in=["Ratones inalámbricos"]).delete()
    
    url = 'https://www.mediamarkt.es/es/category/ratones-inal%C3%A1mbricos-91.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    req = urllib.request.Request(url, headers=headers)
    f = urllib.request.urlopen(req)
    s = BeautifulSoup(f, "lxml")

   # Find all product containers
    product_containers = s.find_all('div', 
                    class_='sc-bf62a61f-0 jFPeRB sc-3e603664-3 eTTzhe sc-66851cef-2 cyydrP')
    
    for container in product_containers:
        # Find the product name within the container
        product_name_tag = container.find('p', class_='sc-8b815c14-0 dbwSez')
        product_price_tag = container.find('span', class_='sc-8b815c14-0 hRgOtg sc-971d7c13-2 gaxNKk')
        if product_name_tag and product_price_tag:
            product_name = product_name_tag.get_text(strip=True)
            product_price = product_price_tag.get_text(strip=True)
            print(product_name)
            print(product_price+"\n")
        elif product_name_tag:
            #Check the other class for the price
            product_price_tag = container.find('span', class_='sc-8b815c14-0 kcIOQy sc-971d7c13-2 gaxNKk')
            
            product_name = product_name_tag.get_text(strip=True)
            product_price = product_price_tag.get_text(strip=True)
            print(product_name)
            print(product_price+"\n")
        else:
            print("Product not found")
        
        # Parse the price
        if "–" in product_price:
            product_price = float(product_price.replace('€', '').replace(',', '.').replace("–","00").replace('-','00').strip())
        else:
            product_price = float(product_price.replace('€', '').replace(',', '.').strip())

        # Create a new category for the product
        category_name = "Ratones inalámbricos"
        category_slug = re.sub(r'\s+', '-', category_name.lower()).replace('á', 'a')
        category, created = Category.objects.get_or_create(name=category_name, slug=category_slug)

        # Create a new product
        product_slug = re.sub(r'\s+', '-', product_name.lower()).replace('á', 'a')
        product_slug = product_slug.replace('ó', 'o').replace(',', '-').replace('ñ', 'n').replace('í', 'i').replace('ú', 'u').replace('é', 'e').replace('º', '').replace('ª', '').replace('ç', 'c').replace('ü', 'u').replace(' ', '-').replace('(', '').replace(')', '').replace('?', '').replace('¿', '').replace('¡', '').replace('!', '').replace(';', '').replace(':', '').replace('.', '').replace('´', '').replace('`', '')
        product, created = Product.objects.get_or_create(
            category=category,
            name=product_name.split(',')[0],
            slug=product_slug,
            price=product_price,
            image='raton-inalambrico.jpg',
            description=product_name
        )




