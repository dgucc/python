# pip install --upgrade pip
# pip install requests
# pip freeze
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)
#print(soup.find_all("a", class_='govuk-link'))
#print(soup.find(id='logo'))

class_name = "gem-c-document-list__item-title"
titres = soup.find_all("a", class_=class_name)
titres_text = []
for titre in titres:
	titres_text.append(titre.string)
#print(titres_text)


class_name = "gem-c-document-list__item-description"
descriptions = soup.find_all("p", class_=class_name)
descriptions_text = []
for description in descriptions:
	descriptions_text.append(description.string)
#print(descriptions_text)

headers=["titre","description"]
with open("gov_uk.csv", "w") as out_csv:
	writer = csv.writer(out_csv, delimiter=',')
	writer.writerow(headers)
	for titre, description in zip(titres_text, descriptions_text):
		line = [titre, description]
		writer.writerow(line)

