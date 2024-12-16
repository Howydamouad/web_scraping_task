import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.baraasallout.com/test.html"  # هنا بحط اللينك بتاع الصفحة بتاعتي
response = requests.get(url)  # هنا بعمل طلب عشان أجيب الصفحة

if response.status_code == 200:
    html_content = response.text  # عشان أضمن أن الصفحة شغالة كويس
    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find('table')

    headers = [header.get_text(strip=True)
          for header in table.find_all('th')] #strip = true دي عشان اشيل المسافات بدايه ونهايه الكلمه

    rows = [] # دي عشان اخزن كل ال rows
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        row_data = [col.get_text(strip=True) for col in columns]
        rows.append(row_data)

    with open('Extracted_Table_Data.csv', mode='w', newline='', encoding='utf-8') as file:
          writer = csv.writer(file)
          writer.writerow(headers)
          writer.writerows(rows)
