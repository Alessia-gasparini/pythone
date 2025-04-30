import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")

import bs4
doc = bs4.BeautifulSoup(text,"html.parser")
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag :
        tds = tr.contents
        sigl =      tds[7].get_text()
        prov =      tds[1].get_text()
        resi =  int(tds[2].get_text().replace(".",""))
        km4 =   int(tds[4].get_text().replace(".",""))
        dens =  float(resi / km4)
        print(f"{sigl} {prov:25s} {resi:9d} {km4} {dens:2f}")