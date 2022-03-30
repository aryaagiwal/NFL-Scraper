import bs4 as bs
from urllib.request import Request, urlopen
import ssl
import pandas as pd
import numpy as np

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
    ties = []
    pfs, pas, hrs, rrs, drs, cfrs, nfcrs, ss, lfs = [], [], [], [], [], [], [] ,[] ,[]
    for table in soup.find_all("table"):
        for body in table.find_all("tbody"):
            for row in table.find_all("tr"):
                #names.append(row.find("div", {"class" : "d3-o-club-fullname"}).get_text())
                tds = row.find_all("td")
                for td_idx, td in enumerate(tds):
                    if td_idx % 18 == 0:
                        names.append(td.get_text().strip().split('\n')[0])
                    if td_idx % 18 == 1:
                        wins.append(int(td.get_text()))
                    if td_idx % 18 == 2:
                        losses.append(int(td.get_text()))
                    if td_idx % 18 == 3:
                        ties.append(int(td.get_text()))
                    if td_idx % 18 == 5:
                        pfs.append(int(td.get_text()))
                    if td_idx % 18 == 6:
                        pas.append(int(td.get_text()))
                    if td_idx % 18 == 8:
                        hrs.append(td.get_text())
                    if td_idx % 18 == 9:
                        rrs.append(td.get_text())
                    if td_idx % 18 == 10:
                        drs.append(td.get_text())
                    if td_idx % 18 == 12:
                        cfrs.append(td.get_text())
                    if td_idx % 18 == 14:
                        nfcrs.append(td.get_text())
                    '''
                                        if td_idx % 18 == 15:
                        if (td.get_text()[-1] == 'L'):
                            ss.append(int(td.get_text()[:-1]) * -1)
                        else:
                            ss.append(int(td.get_text()[:-1]))
                    '''

                    if td_idx % 18 == 16:
                        lfs.append(td.get_text())
    data_dict = {
        "Names" : names,
        "Wins" : wins,
        "Losses" : losses,
        "Ties" : ties,
        "Points For" : pfs,
        "Points Against" : pas,
        "Home Record" : hrs,
        "Road Record" : rrs,
        "Conference Record" : cfrs,
        "Non-Conference Record" : nfcrs
    }
    data_df = pd.DataFrame(data_dict)
    data_df.to_csv("./standings.csv")

