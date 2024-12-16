import json # بعمل import لملف json
import requests
from bs4 import BeautifulSoup

url = "https://www.baraasallout.com/test.html"  # هنا بحط اللينك بتاع الصفحة بتاعتي
response = requests.get(url)  # هنا بعمل طلب عشان أجيب الصفحة

if response.status_code == 200:
    html_content = response.text  # عشان أضمن أن الصفحة شغالة كويس
    soup = BeautifulSoup(html_content, "html.parser")

    product_card = soup.find_all('div',class_= 'product-card') # هنا حطيت الكلاس لانه الحاجه المميزه
    book_data = []
    for card in product_card :
        Book_Title = card.find('p',class_='name').get_text(strip=True) if card.find('p', class_='name') else "not found" #هنا عملت شرط عشان اتاكد موجود ولا لا

        price = card.find('p', class_='price').get_text(strip=True) if card.find('p',class_='price') else "not found"

        stock = card.find('p', class_='instock_availability').get_text(strip=True) if card.find('p',class_='stock') else "not found"

        button = card.find('button')
        button_text = button.get_text(strip=True) if button else "N/A"

        book_data.append({ # هنا بعمل append للبيانات عندي
          'Book Title':Book_Title ,
          'Price': price,
          'Stock Availability': stock,
          'Button Text': button_text
        })
    with open('Product_Information.json', mode='w', encoding='utf-8') as file:
        json.dump(book_data, file, ensure_ascii=False, indent=4)
        #  json.dump دي المكتبه
        #ensure_ascii=False عشان ميحولش الحاجه لل ascii code
        # indent=4 بيظيط الملف وبيحط مسافه 4
