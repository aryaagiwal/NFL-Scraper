import bs4 as bs
from urllib.request import Request, urlopen
import ssl

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    req = Request("https://www.nfl.com/standings/division/2020/REG")
    web_page = urlopen(req).read()
    soup = bs.BeautifulSoup(web_page, 'lxml')
    division_names = [table.find("th", {"aria-label" : "Division name"}).get_text()
                      for table in soup.find_all("table")]
    names = []
    wins = []
    losses = []
    for table in soup.find_all("table"):
        for body in table.find_all("tbody"):
            for row in table.find_all("tr"):
                for td in row.find_all("td"):
                    print(td.get_text())
            '''
            for a in body.find_all("a", {"class" : "d3-o-club-info"}):

                print(a.find("div", {"class" : "d3-o-club-fullname"}).get_text())
            tds = [body.find_all("td")]
            print(tds)'''
                

