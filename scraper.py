import requests
from bs4 import BeautifulSoup

URL = "https://www.nfl.com/standings/division/2020/REG"
page = requests.get(URL)

#print(page.text)
standings = BeautifulSoup(page.content, "html.parser")

#print (standings.prettify())
standings_body = standings.body
standings_main = standings.find(id="main-content")
#print(standings_main.prettify)
standings_data = standings_main.next_element.next_element.next_element.next_element.next_element.next_sibling.next_sibling.next_sibling.next_sibling.next_element.next_element.next_element.next_element.next_element.next_element
standings_afceast = standings_data.next_element.next_element
standings_afcnorth = standings_afceast.next_sibling.next_sibling
standings_afcsouth = standings_afcnorth.next_sibling.next_sibling
standings_afcwest = standings_afcsouth.next_sibling.next_sibling
standings_centerad = standings_afcsouth.next_sibling.next_sibling.next_sibling.next_sibling
standings_nfceast = standings_centerad.next_sibling.next_sibling
standings_nfcnorth = standings_nfceast.next_sibling.next_sibling
standings_nfcsouth = standings_nfcnorth.next_sibling.next_sibling
standings_nfcwest = standings_nfcsouth.next_sibling.next_sibling

#at this point, each of the 8 standings subdivisons contains data on the respective conference
#print(standings_afceast)