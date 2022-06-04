# Webscraping with python + csv export
# 
# Purposes : fetch alls "Themes" fr-nl from website and export them in csv
# Remarks : 
#   url fr <> nl; 
#   labels are stored in anchors <a>;
#   labels are identified by a GUID cf. href attribute (need some extra parsing);
#   some labels contain "," => use ";" as separator in csv
# 
# Pre-requesites :
# python3 -m pip install --upgrade pip
# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv

# requests to ccrek website 
# return BeautifulSoup response
def getSoupParser(lang):
    url = ""
    if lang=="fr":
        url = "https://www.rekenhof.be/FR/Publications/Themes.html" 
    else:
        url = "https://www.rekenhof.be/NL/Publicaties/Themas.html"
    
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# fetch theme's id and fr labels
soup = getSoupParser("fr")
anchors = soup.select("div.thema a");

labels = []
for anchor in anchors:
    id=anchor['href'].split('=')[1]
    label=anchor.text
    labels.append({'id':id, 'fr':label})

# fetch theme's id and nl labels
soup = getPageContent("nl")
anchors = soup.select("div.thema a");

for anchor in anchors:
    id=anchor['href'].split('=')[1]
    label=anchor.text
    # retrieve existing id in list of labels
    # add "nl" property and value
    obj = list(filter(lambda x: x['id']==id, labels))[0]
    obj['nl'] = label

# export into csv
headers=["id","fr","nl"]
with open("themes.csv", "w") as out_csv:
    writer = csv.writer(out_csv, delimiter=';')
    writer.writerow(headers)
    for label in labels:
        writer.writerow(label.values())
