import json # بعمل import لملف json
import requests
from bs4 import BeautifulSoup

url = "https://www.baraasallout.com/test.html"  # هنا بحط اللينك بتاع الصفحة بتاعتي
response = requests.get(url)  # هنا بعمل طلب عشان أجيب الصفحة

if response.status_code == 200:
    html_content = response.text  # عشان أضمن أن الصفحة شغالة كويس
    soup = BeautifulSoup(html_content, "html.parser")
links_data = []
links = soup.find_all('a')
for link in links:
    href = link.get('href', 'not found')
    text = link.get_text(strip=True)
    if href != 'not found':
        links_data.append({
            "Type": "Hyperlink",
            "Text": text,
            "URL": href
        })


iframe_data = []
iframes = soup.find_all('iframe')
for iframe in iframes:
    src = iframe.get('src', 'N/A')
    if src != 'N/A':
        iframe_data.append({
            "Type": "Video",
            "URL": src
        })

all_data = links_data + iframe_data

with open('Links_and_Multimedia.json', mode='w', encoding='utf-8') as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)

