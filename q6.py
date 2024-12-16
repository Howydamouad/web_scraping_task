import json # بعمل import لملف json
import requests
from bs4 import BeautifulSoup

url = "https://www.baraasallout.com/test.html"  # هنا بحط اللينك بتاع الصفحة بتاعتي
response = requests.get(url)  # هنا بعمل طلب عشان أجيب الصفحة

if response.status_code == 200:
    html_content = response.text  # عشان أضمن أن الصفحة شغالة كويس
    soup = BeautifulSoup(html_content, "html.parser")
featured_products_data = []
products = soup.find_all('div', class_='product-card')

for product in products:

    name = product.find( class_='name')
    name = name.get_text(strip=True) if name else 'N/A'

    price = product.find( class_='price', style="display: none;")
    price = price.get_text(strip=True) if price else 'N/A'

    colors = product.find( class_='colors')
    colors = colors.get_text(strip=True) if colors else 'N/A'

    product_id = product.get('data-id', 'N/A')

    featured_products_data.append({
        "Product Name": name,
        "Hidden Price": price,
        "Available Colors": colors,
        "Product ID": product_id
    })

with open('Featured_Products.json', mode='w', encoding='utf-8') as file:
    json.dump(featured_products_data, file, ensure_ascii=False, indent=4)
