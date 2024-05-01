from bs4 import BeautifulSoup
import json
import requests
from bs4.element import Doctype, NavigableString

def html_to_json(tag):
    if not tag:
        return None
    if isinstance(tag, slice):
        return {
            
        }
    if isinstance(tag, Doctype):
        return {
            "type": "doctype",
            "name": tag.name,
        }
    if isinstance(tag, NavigableString):
        return str(tag)
    return {
        "tag": tag.name,
        "attrs": dict(tag.attrs),
        "text": tag.string,
        "children": [html_to_json(child) for child in tag.children]
    }

 #pg1 code
pagenum=0
job=input('what position u looking for:')
job = job.replace(" ","-")
url =f'https://www.linkedin.com/jobs/{job}-jobs?keywords=Qa%20Tester&location=United%20States&geoId=103644278&f_TPR=r604800&position=1&pageNum=0'
 #user inputs positions and grab job ids of each page
    #html to json
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')


# # Convert the BeautifulSoup object to a JSON string
json_content = json.dumps(html_to_json(soup), indent=4)

with open('./job1.json','w') as file:
     file.write(json_content)
    
    
 