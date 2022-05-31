import csv
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import datefinder

csvfile = 'inputCSV/source_claims.csv'
csvoutput= 'outputCSV/test.csv'
with open(csvfile) as inputData, open('test.csv', 'w+') as fout:
    header = ["Annotations","Score","CR Author A","CR Author B","Review URL A","Review URL B",
    "Text Fragments A","Text Fragments B","Entities A","Entities B", "Keywords A", "Keywords B",
    "Author Text A", "Author Text B", "Date Text A", "Date Text B", "Url A keywords", "Url B keywords"]
    writer = csv.writer(fout)
    reader = csv.reader(inputData)
    claims = list(reader)
    writer.writerow(header)
    for row in claims:
        if row[2][0]=="p":
            col = []
            url = row[4]
            url2 = row[5]

            # suppression des 4 dernieres colonnes
            row = row[:-4]

            # ouverture de la page
            page = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
            page2 = urlopen(Request(url2, headers={'User-Agent': 'Mozilla'}))

            # on charge le code la page
            codedelap = bs(page, features="html.parser")
            codedelap2 = bs(page2, features="html.parser")

            # recuperation de l'auteur
            nom_auteur = codedelap.find("a", class_="m-statement__name").get_text()
            nom_auteur2 = codedelap2.find("a", class_="m-statement__name").get_text()
            col.append(nom_auteur[1:-2])
            col.append(nom_auteur2[1:-2])

            # recuperation date
            date_ = codedelap.find("div", class_="m-statement__desc").get_text()
            date_2 = codedelap2.find("div", class_="m-statement__desc").get_text()

            #transformation de la variable de tpe datetime
            match = datefinder.find_dates(date_)
            for m in match:
                col.append(m.strftime("%Y-%m-%d"))
                break
            match2 = datefinder.find_dates(date_2)
            for m in match2:
                col.append(m.strftime("%Y-%m-%d"))
                break

            #recuperation de la claim
            claim1 = codedelap.find("h2", class_="c-title c-title--subline").get_text()
            claim2 = codedelap2.find("h2", class_="c-title c-title--subline").get_text()
            row[6] = claim1[1:-1]
            row[7] = claim2[1:-1]

            #recupération des mots clés
            listmc = ""
            listmc2 = ""
            mc = codedelap.find_all("a", class_="c-tag")
            mc2 = codedelap2.find_all("a", class_="c-tag")
            for lien in mc:
                txt = lien.find("span")
                if listmc == "":
                    listmc += txt.get_text()
                else:
                    listmc += ","+txt.get_text()
            for lien in mc2:
                txt = lien.find("span")
                if listmc2 == "":
                    listmc2 += txt.get_text()
                else:
                    listmc2 += "," + txt.get_text()
            col.append(listmc)
            col.append(listmc2)
            writer.writerow(row + col)
print("done.")