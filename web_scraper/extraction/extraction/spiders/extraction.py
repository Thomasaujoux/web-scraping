import scrapy
from ..items import DistributeurItem
from datetime import datetime
import json


class DistributeurSpider(scrapy.Spider):
    name = "Distributeur"

    def __init__(self, *args, **kwargs):
        super(DistributeurSpider, self).__init__(*args, **kwargs)
        with open(self.results, "rt") as f:
            self.start_urls = [json.loads(url)['url'] for url in f.readlines()]

    def parse(self, response):
        for i in range(3):
            print("\n test \n")
        item=DistributeurItem()
        item["horloge"]=str(datetime.now())
        item["url"]=response.url
        item["html"]=response.css("html").get()
        if "www.auchan.fr" in response.url:
            item["distributeur"]="Auchan"
            item["prix"]="null"
            nom = response.css("span.site-breadcrumb__item--last h1 a::text").get()
            item["nom"]=nom
            #prix=response.css("div.product-price::text").getall()
            #print(prix)
            #item["prix"]=prix[1]
            quantite=response.css("div.offer-selector__description-content span.product-attribute::text").get()
            print(quantite)
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
            
            groupe1_1=response.css("div.product-description__feature-wrapper")
            groupe1_2=groupe1_1.css("div.product-description__feature--single")
            groupe1_3=[]
            groupe1R=[]
            for element in groupe1_2:
                donnee=element.css("span.product-description__feature-value::text").getall()
                groupe1_3+=donnee
                repere_1=element.css("h5.product-description__feature-title::text").getall()
                repere_2=element.css("div h3::text").getall()
                groupe1R+=repere_1
                groupe1R+=repere_2
            print(groupe1_3)
            print(groupe1R)

            saison=response.css("div.offer-selector__description-header span.product-flap__label::text").getall()
            label=response.css("div.product-picto__text::text").getall()       # à demander
            if "Format" in label:
                label.remove("Format")
            if "C'est de saison !" in saison:
                label.append("C'est de saison !")
            item["label"]=label
            v_nut_1=response.css("td.nutritionals__cell::text").getall()
            for i in range (len(v_nut_1)):
                v_nut_1[i]=v_nut_1[i].replace("\n","")
                v_nut_1[i]=v_nut_1[i].replace(" ","")
            if len(v_nut_1)>14:
                v_nut={"Valeur énergétique" : v_nut_1[1], "Matières grasses" : v_nut_1[5],
                "dont Acides gras saturés" : v_nut_1[7],"Glucides" : v_nut_1[9], "dont Sucres" : v_nut_1[11],"Protéines" : v_nut_1[13],"Sel" : v_nut_1[15]}
                item["valeurs_nutritionelles"]=v_nut
            else:
                item["valeurs_nutritionelles"]=None
            fil_ariane_1=response.css("nav.site-breadcrumb__nav")
            fil_ariane=fil_ariane_1.css("a::text").getall()
            item["fil_ariane"]=fil_ariane[1:]

        else:
            item["distributeur"]="Franprix"
            nom=response.css("h1.font-semibold::text").get()
            item["nom"]=nom.split("\n")[1].strip()
            prix=response.css("span.product-item-priceperkilo::text").get()
            item["prix"]=prix
            quantite=response.css("div.block::text").get()
            item["quantite"]=quantite.split("\n")[0].strip()
            industriel_1=response.css("div.block")
            industriel=industriel_1.css("span::text").get()
            item["industriel"]=industriel
            reference_1=response.url
            reference_2=reference_1.split("-")
            reference=reference_2[-1]
            item["reference"]=reference


            # nécessite de toucher au JS.
            """
            groupe0_1=response.css("div.product-tab space-y-3")
            groupe0=groupe0_1.css("div")
            description_marketing=groupe0_1.css("div::text").getall()
            origine=groupe0[1].css("span::text").getall()
            print(description_marketing)
            print(origine)
            conservation=response.css("span.font-semibold::text").getall()
            description_legale
            ingredients
            valeur_nutritionnelle


            """
            groupe_1=response.css("img.transition-all").xpath("@src").getall()
            label=groupe_1.copy()
            EAN=groupe_1[0][42:55]
            item["EAN"]=EAN
            item["label"]=label
            fil_ariane_1=response.css("li.breadcrumb-item")
            fil_ariane=[]
            for e in fil_ariane_1:
                text_elt = e.css("a::text").get()
                if text_elt:
                    text_elt = text_elt.split("\n")[1].strip()
                    fil_ariane.append(text_elt)
            item["fil_ariane"]=fil_ariane

        yield item