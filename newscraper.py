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
    pfs, pas, hrs, rrs, drs, cfrs, ncfrs, ss, lfs = [], [], [], [], [], [], [] ,[] ,[]
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
                        ncfrs.append(td.get_text())
                    '''
                                        if td_idx % 18 == 15:
                        if (td.get_text()[-1] == 'L'):
                            ss.append(int(td.get_text()[:-1]) * -1)
                        else:
                            ss.append(int(td.get_text()[:-1]))
                    '''

                    if td_idx % 18 == 16:
                        lfs.append(td.get_text())

    hw = []
    hl = []
    ht = []

    rw = []
    rl = []
    rt = []

    dw = []
    dl = []
    dt = []

    cw = []
    cl = []
    ct = []

    ncw = []
    ncl = []
    nct = []

    lw = []
    ll = []
    lt = []

    for val in hrs:
        hw.append(int(val.strip().split(" - ")[0]))
        hl.append(int(val.strip().split(" - ")[1]))
        ht.append(int(val.strip().split(" - ")[2]))

    for val in rrs:
        rw.append(int(val.strip().split(" - ")[0]))
        rl.append(int(val.strip().split(" - ")[1]))
        rt.append(int(val.strip().split(" - ")[2]))

    for val in drs:
        dw.append(int(val.strip().split(" - ")[0]))
        dl.append(int(val.strip().split(" - ")[1]))
        dt.append(int(val.strip().split(" - ")[2]))

    for val in cfrs:
        cw.append(int(val.strip().split(" - ")[0]))
        cl.append(int(val.strip().split(" - ")[1]))
        ct.append(int(val.strip().split(" - ")[2]))

    for val in ncfrs:
        ncw.append(int(val.strip().split(" - ")[0]))
        ncl.append(int(val.strip().split(" - ")[1]))
        nct.append(int(val.strip().split(" - ")[2]))

    for val in lfs:
        lw.append(int(val.strip().split(" - ")[0]))
        ll.append(int(val.strip().split(" - ")[1]))
        lt.append(int(val.strip().split(" - ")[2]))

    data_dict = {
        "Names" : names,
        "Wins" : wins,
        "Losses" : losses,
        "Ties" : ties,
        "Points For" : pfs,
        "Points Against" : pas,
        "Home Wins" : hw,
        "Home Losses" : hl,
        "Home Ties" : ht,
        "Road Wins" : rw,
        "Road Losses" : rl,
        "Road Ties" : rt,
        "Division Wins" : dw,
        "Division Losses" : dl,
        "Division Ties" : dt,
        "Conference Wins" : cw,
        "Conference Losses" : cl,
        "Conference Ties" : ct,
        "Non-Conference Wins" : ncw,
        "Non-Conference Losses" : ncl,
        "Non-Conference Ties" : nct,
        "Last Five Wins" : lw,
        "Last Five Losses" : ll,
        "Last Five Ties" : lt
    }
    data_df = pd.DataFrame(data_dict)
    data_df.to_csv("./standings.csv")