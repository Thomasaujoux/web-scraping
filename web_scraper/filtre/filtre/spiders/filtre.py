import scrapy
import fileinput
from ..items import FiltreItem
from os import listdir
from os.path import isfile, join
import json
import pandas as pd

class Filtre(scrapy.Spider):
    name = "Filtre"

    def start_requests(self):
        fichiers_rayons = [f for f in listdir(self.rayons) if isfile(join(self.rayons, f))]
        fichiers_urls = [f for f in listdir(self.urls) if isfile(join(self.urls, f))]
        print("=====")
        print(self.urls)
        liste = json.loads(self.params)
        for rayons in fichiers_rayons:
            fichier_rayons=open(self.rayons+"/"+rayons,"r",encoding="utf-8")
            rayons_lus=fichier_rayons.read()
            chemin=rayons_lus.split("\n")
            fichier_rayons.close()
            for key in liste.keys():
                mag = rayons.split("rayons_")[1]
                if key == mag:
                    nbrayons = liste[key]['nbrayons']
                    selecteur = liste[key]['selecteur']
                    for urls in fichiers_urls:
                        mag_url = urls.split("urls_")[1].split(".jl")[0]
                        if mag == mag_url:
                            fichier_urls = self.urls + "/" + urls
                            print("-----------")
                            print(fichier_urls)
                            break
                    break

            url_base = "https://www."+mag+".fr"
            df=pd.read_json(self.urls,lines=True)
            for i in range (len(df)):
                url_origin=str(df.loc[i,"url_base"])
                url_suite=str(df.loc[i,"url"])
                if url_origin != "nan":
                    if url_suite[0] == "/":
                        url=url_base+url_suite
                        yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(nbrayons=nbrayons,selecteur=selecteur,chemin=chemin))    


    def parse(self, response, nbrayons, selecteur, chemin):
        item=FiltreItem()
        #fil_ariane=response.css("nav.site-breadcrumb__nav a::text").getall()
        fil_ariane=response.css(selecteur).getall()
    
        fil_ariane_formated = [] 
        for x in fil_ariane:
            if "\n" in x:
                fil_ariane_formated.append(x.split("\n")[1].strip())
            else:
                fil_ariane_formated.append(x)

        if len(fil_ariane_formated)>int(nbrayons):
            for x in range(int(nbrayons)):
                if fil_ariane_formated[x+1] in chemin:
                    url=response.url
                    item["url"]=url
                    yield item