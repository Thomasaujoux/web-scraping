import scrapy
import fileinput
from ..items import DistributeurItem
from os import listdir
from os.path import isfile, join
import json
import pandas as pd
from datetime import datetime
import logging
from scrapy.utils.log import configure_logging
import js2py

class DistrubuteurSpider(scrapy.Spider):
    name = "Distributeur"

    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log-'+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+'.txt',
        format='%(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    def start_requests(self):
        fichiers_rayons = [f for f in listdir(self.rayons) if isfile(join(self.rayons, f))]
        fichiers_urls = [f for f in listdir(self.urls) if isfile(join(self.urls, f))]
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
                            break
                    break

            url_base = "https://www."+mag+".fr"
            df=pd.read_json(fichier_urls,lines=True)
            for i in range (len(df)):
                url_origin=str(df.loc[i,"url_base"])
                url_suite=str(df.loc[i,"url"])
                
                if url_origin != "nan":
                    if url_suite[0] == "/":
                        url=url_base+url_suite
                    else:
                        url=url_suite
                    logging.debug('---'+url)
                    yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(nbrayons=nbrayons,selecteur=selecteur,chemin=chemin))



    def parse(self, response, nbrayons, selecteur, chemin):
        logging.debug('==='+response.url)
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
                    logging.debug('***'+response.url)
                    item=DistributeurItem()
                    item["horloge"]=str(datetime.now())
                    item["url"]=response.url
                    item["html"]=response.css("html").get()
                    # Si le distributeur est Auchan.
                    if "www.auchan.fr" in response.url:
                        item["distributeur"]="Auchan"
                        item["prix"]="null"
                        nom = response.css("span.site-breadcrumb__item--last h1 a::text").get()
                        item["nom"]=nom
                        #prix=response.css("div.product-price::text").getall()
                        #print(prix)
                        #item["prix"]=prix[1]
                        quantite=response.css("div.offer-selector__description-content span.product-attribute::text").get()
                        item["quantite"]=quantite
                        #origine=response.css("div.product-detail::text").get()
                        #print(origine)
                        #item["origine"]=origine
                        groupe0_1=response.css("div.product-description__feature-values::text").get()   # contient reference et EAN
                        groupe0=groupe0_1.split(" / ")
                        for i in range (len(groupe0)):
                            groupe0[i]=groupe0[i].replace("\n","")
                            groupe0[i]=groupe0[i].replace(" ","")
                        reference=groupe0[0]
                        EAN=groupe0[1:]
                        item["reference"]=reference
                        item["EAN"]=EAN
                        
                        groupe1_1=response.css("div.product-description__feature-wrapper div")
                        groupe1_2=[]
                        for e in groupe1_1:
                            element=e.css("span::text").getall()
                            groupe1_2.append(element)
                        groupe1R_1=response.css("div.product-description__feature-wrapper div div")
                        groupe1R=[]
                        for e in groupe1R_1:
                            element1=e.css("h5::text").getall()
                            element2=e.css("h3::text").getall()
                            groupe1R+=element1
                            groupe1R+=element2
                        for i,e in enumerate(groupe1R):
                            if e=="Pays d'origine":
                                item["origine"]=groupe1_2["i"]
                            elif e=="Description marketing" or e=="Marketing" or e=="Descriptif Commercial" or e=="Avantages produit":
                                item["description_marketing"]=groupe1_2[i]
                            elif e=="Informations pratiques":
                                if groupe1_2[i][0]=="Conditions particulières de conservation":
                                    item["conservation"]=groupe1_2[i][1]
                                    item["conseil_preparation"]=groupe1_2[i][3]
                                else:
                                    item["conservation"]=groupe1_2[i][3]
                                    item["conseil_preparation"]=groupe1_2[i][1]
                            elif e=="Dénomination légale de vente":
                                item["description_legale"]=groupe1_2[i]
                            elif e=="Conditions particulières de conservation":
                                item["conservation"]=groupe1_2[i]
                            elif e=="Ingrédients":
                                item["ingredients"]=groupe1_2[i]
                            elif e=="Contact" or e=="Exploitant":
                                item["industriel"]=groupe1_2[i]
                            elif e=="Mode d'emploi":
                                item["conseil_preparation"]=groupe1_2[i]
                        allergene=response.css("span.product-features__value::text").get()
                        item["allergene"]=allergene
                        label_1=response.css("div.offer-selector__description-header span.product-flap__label::text").getall()
                        label_2=response.css("div.product-picto__text::text").getall()
                        if "Format" in label_2:
                            label_2.remove("Format")
                        item["label"]=label_1+label_2
                        v_nut_1=response.css("td.nutritionals__cell::text").getall()
                        for i in range (len(v_nut_1)):
                            v_nut_1[i]=v_nut_1[i].replace("\n","")
                            v_nut_1[i]=v_nut_1[i].strip(" ")
                        if len(v_nut_1)>2:
                            v_nut={}
                            for i in range(len(v_nut_1)-1):
                                if v_nut_1[i] in ["Matières grasses","dont Acides gras saturés","Glucides",
                                                  "dont Sucres","Protéines","Sel","Fibres alimentaires"]:
                                    v_nut[v_nut_1[i]]=v_nut_1[i+1]
                                elif v_nut_1[i] in ["Valeur énergétique"]:
                                    if v_nut_1[i+1][-1]=="J":
                                        v_nut[v_nut_1[i]+"kJ"]=v_nut_1[i+1]
                                    elif v_nut_1[i+1][-1]=="l":
                                        v_nut[v_nut_1[i]+"kcal"]=v_nut_1[i+1]
                            item["valeurs_nutritionnelles"]=v_nut

                    # Si le distributeur est Franprix
                    else:
                        item["distributeur"]="Franprix"
                        nom=response.css("h1.font-semibold::text").get()
                        item["nom"]=nom.split("\n")[1].strip()
                        prix=response.css("span.product-item-priceperkilo::text").get()
                        item["prix"]=prix
                        quantite=response.css("div.block::text").get()
                        item["quantite"]=quantite.split("\n")[0].strip()
                        #industriel_1=response.css("div.block")
                        #industriel=industriel_1.css("span::text").get()
                        #item["industriel"]=industriel
                        reference_1=response.url
                        reference_2=reference_1.split("-")
                        reference=reference_2[-1]
                        item["reference"]=reference
                        script_js=response.css("body script::text").get()
                        script=js2py.eval_js(script_js)["data"][0]["product"]
                        scriptR=str(script)
                        if "brand" in scriptR:
                            item["industriel"]=script["brand"]
                        if "allergy" in scriptR:
                            item["allergene"]=script["allergy"]
                        if "conservation" in scriptR:
                            item["conservation"]=script["conservation"]
                        if "desc" in scriptR:
                            item["description_legale"]=script["desc"]
                        v_nut={}
                        if "energy_kcal" in scriptR:
                            v_nut["Valeur énergétique (kcal)"]=script["energy_kcal"]["amount"]
                        if "energy_kj" in scriptR:
                            v_nut["Valeur énergétique (kJ)"]=script["energy_kj"]["amount"]
                        if "nutri_fat" in scriptR:
                            v_nut["Matières grasses"]=script["nutri_fat"]["amount"]
                        if "nutri_sat_fat" in scriptR:
                            v_nut["dont Acides gras saturés"]=script["nutri_sat_fat"]["amount"]
                        if "nutri_carbohy" in scriptR:
                            v_nut["Glucides"]=script["nutri_carbohy"]["amount"]
                        if "nutri_sugar" in scriptR:
                            v_nut["dont Sucres"]=script["nutri_sugar"]["amount"]
                        if "nutri_protein" in scriptR:
                            v_nut["Protéines"]=script["nutri_protein"]["amount"]
                        if "nutri_salt" in scriptR:
                            v_nut["Sel"]=script["nutri_salt"]["amount"]
                        if "Fiber" in scriptR:
                            v_nut["Fibre"]=script["Fiber"]["amount"]
                        item["valeurs_nutritionnelles"]=v_nut
                        if "ingredient" in scriptR:
                            item["ingredients"]=script["ingredient"]
                        if "marketing_text" in scriptR:
                            item["description_marketing"]=script["marketing_text"]
                        if "origin" in scriptR:
                            item["origine"]=script["origin"]
                        if "preparation" in scriptR:
                            item["conseil_preparation"]=script["preparation"]
                        nutri_score=response.css("div.nutri-score span.active::text").get()
                        item["nutri_score"]=nutri_score
                        groupe_1=response.css("img.transition-all").xpath("@src").getall()
                        label=groupe_1.copy()
                        EAN=groupe_1[0][42:55]
                        item["EAN"]=EAN
                        item["label"]=label
                        item["fil_ariane"]=fil_ariane_formated

                    yield item
