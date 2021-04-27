from bs4 import BeautifulSoup
import json
import glob
import urllib.parse




files = glob.glob("tei/*.xml")

files = sorted(files)

for j in range(len(files)):

    # currentPb = initialPbs[j]

    file = files[j]

    if "facs" in file:
        continue

    soup = BeautifulSoup(open(file,'r'), "xml")

    pbs = soup.find_all("pb")

    for pb in pbs:
        del pb["facs"]

    soup.find("facsimile").decompose()

    html = soup.prettify("utf-8")
    with open(file+"_no_facs.xml", "wb") as file:
        file.write(html)