
import csv # هنا كدا بستخرد ملف ال csv
import requests # هنا بستدعي ال request
from bs4 import BeautifulSoup # بستخرج مكتبه ال BeautifulSoup

url = "https://www.baraasallout.com/test.html"  # هنا بحط اللينك بتاع الصفحة بتاعتي
response = requests.get(url)  # هنا بعمل طلب عشان أجيب الصفحة

if response.status_code == 200:
    html_content = response.text  # عشان أضمن أن الصفحة شغالة كويس
    soup = BeautifulSoup(html_content, "html.parser")


    with open('Extract_Text_Data.csv', mode='w', newline='', encoding='utf-8') as files: # هنا بفتح ملف ال csv وبخزن فيه
        writer = csv.writer(files)


        writer.writerow(['h1 Headers', 'h2 Headers', 'Paragraphs', 'List']) # دي الحاجات الي هيقرأها الملف


        headers1 = soup.find_all("h1")
        for header in headers1: # هنا بلف علي كل ال headers
            writer.writerow([header.get_text(), '', '', ''])


        headers2 = soup.find_all("h2")
        for header2 in headers2:
            writer.writerow(['', header2.get_text(), '', ''])


        p_tags = soup.find_all("p")
        for p in p_tags:
            writer.writerow(['', '', p.get_text(), ''])


        li_tags = soup.find_all("li")
        for li in li_tags:
            writer.writerow(['', '', '', li.get_text()])

        with open('Extract_Text_Data.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)