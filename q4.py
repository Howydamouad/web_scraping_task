import json # بعمل import لملف json
import requests
from bs4 import BeautifulSoup

url = "https://www.baraasallout.com/test.html"  # هنا بحط اللينك بتاع الصفحة بتاعتي
response = requests.get(url)  # هنا بعمل طلب عشان أجيب الصفحة

if response.status_code == 200:
    html_content = response.text  # عشان أضمن أن الصفحة شغالة كويس
    soup = BeautifulSoup(html_content, "html.parser")

    form = soup.find_all('form')
    if form:
        forms = form[0]
        inputs = forms.find_all('input')
        input_fields = []
        for field in inputs:
            field_name = field.get('name', 'N/A')
            input_type = field.get('type', 'text')
            default_value = field.get('value', '')

            input_fields.append({
                "Field Name": field_name,
                "Input Type": input_type,
                "Default Value": default_value
            })

        with open('Form_Input_Fields.json', mode='w', encoding='utf-8') as file:
            json.dump(input_fields, file, ensure_ascii=False, indent=4)