############## Informations ##############
"""
Ce fichier comporte la partie crawler de scrapy.
C'est le seul fichier qu'il faut modifier pour scraper sur les différents sites
La documentation pour en apprendre plus dessus se trouve ici : https://docs.scrapy.org/en/latest/topics/spiders.html
"""




############## Importation des librairies ##############
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from w3lib.url import url_query_cleaner


import os
import dotenv

dotenv.load_dotenv()

PAGE = os.environ["PAGE"]
PRODUCTS  = os.environ["PRODUCTS"]
ALLOWEDDOMAINS = os.environ["ALLOWEDDOMAINS"]
STARTURLS = os.environ["STARTURLS"]
BASEURL = os.environ["BASEURL"]
CONCURRENTREQUESTS = os.environ["CONCURRENTREQUESTS"]
DOWNLOADDELAY = os.environ["DOWNLOADDELAY"]
RAYONS = os.environ["RAYONS"].split(',')
#TAGS = os.environ["TAGS"]


############## Process des links ##############
"""
Cette partie contient le moment où on l'on contrôle les liens.
- On peut contraindre de ne pas suivre certains liens : Suivre les liens de produits n'est pas intéressant
- On peut filtrer les liens avec la fonction url_query_cleaner, qui va filtrer les liens déjà vus, elle va filtrer les liens inutiles
- On peut demander de traiter différemment les liens de pages qui auraient été filtrés sinon  
"""
def process_links(links):

    """
    On fait une boucle sur l'ensemble des liens trouvés sur la page
    """
    for link in links:

        """
        On dit de ne pas aller sur les liens des produits
        """
        if PAGE in link.url :
            yield link
        
        elif PRODUCTS in link.url :
            yield

        else :
            link.url = url_query_cleaner(link.url)
            yield link
        """
        On dit de traiter différemment les liens de pages parce que la fonction url_query_cleaner les auraient supprimés.
        La fonction url_query_cleaner est assez complexe, il faut la regarder en détail pour comprendre son fonctionnement
        """





############## On requête les pages ##############
""""
Cette partie va permettre de requêter les pages, elle comporte plusieurs classes qui héritent d'autres classes. 
Pour comprendre le mécanisme regarder la documentation
"""

class myCrawler(CrawlSpider): # Le nom de la classe qui hérite doit être différent de cette classe, ici "myCrawler"
    """
    Nom du projet, à ne pas changer
    """
    name = 'url'
    """
    On restraint le crawling à certains domaines
    """
    allowed_domains = [ALLOWEDDOMAINS]
    """
    On définit l'URL par lequel on commence
    CETTE PARTIE EST A CHANGER EN FONCTION DU SITE
    """
    start_urls = [STARTURLS]
    """
    Cette partie permet juste de moins charger la base de donnée qui n'affichera pas l'ensemble de l'URL mais juste le sous domaine
    CETTE PARTIE EST A CHANGER EN FONCTION DU SITE
    """
    base_url = BASEURL


    """
    Cette partie concerne la façon dont nous allons faire les requêtes, de manière à ne pas être bloqué par le site
    """
    custom_settings = {
        # 'DOWNLOADER_MIDDLEWARES' est inutile dans notre cas, mais je le laisse car on pourrait l'utiliser pour d'autres sites
        #'DOWNLOADER_MIDDLEWARES': {'tempbuffer.middlewares.RotateUserAgentMiddleware': 400, },

        # Toujours les enlever, permet de moins se faire repérer
        'COOKIES_ENABLED': False,
        # C'est le nombre de requêtes que l'on fait en même temps, par défaut 16 je crois
        'CONCURRENT_REQUESTS': CONCURRENTREQUESTS,
        # C'est les délais que nous allons rajouter, les délais sont automatiques aléatoires +/- 0.5 sec
        'DOWNLOAD_DELAY': DOWNLOADDELAY,

        # On passe à la partie pipeline qui permet de stocker l'information, mais pour notre cas c'est pas vraiment utile
        # This settings are a must: donc je les ai enlevés
        # Duplicates pipeline
        #'ITEM_PIPELINES': {'pipelines.DuplicatesPipeline': 300},

        # In order to create a CSV file: en réalité on crée un json avec la commande, donc inutile mais je laisse si jamais
        #'FEEDS': {'csv_file.csv': {'format': 'csv'}}
    }

    """
    Cette partie concerne les régles que nous allons établir pour les requêtes.
    Attention c'est un tuple de Python donc dans certains cas il faudra rajouter des "," ou non
    """
    rules = (
        Rule(
            LinkExtractor(allow_domains=ALLOWEDDOMAINS, allow = RAYONS, tags= ("link","a", "area")),
            # Renvoie à notre fonction discutée précédemment
            process_links=process_links,
            # Une fois la page requêtée, cette fonction permet de traiter les informations que nous allons garder
            callback='parse_item',
            follow=True
        ),
    )

            

############## On récupére les informations sur les pages ##############
    def parse_item(self, response):

        """
        Permet de savoir quelles pages on a requêtées
        """
        print(response)

        """
        Prend tous les liens URLs de la page
        """
        all_urls = response.css('a::attr(href)').getall()

        # In order to change from relative to absolute url in the pipeline: Pas utile parce que on a enlevé la pipeline précédemment
        #self.base_url = response.url

        """
        On récupére uniquement les liens des produits
        """
        for url in all_urls :
            if PRODUCTS in url: 
                yield{
                    'url': url,
                    'url_base': response.url
                    }




    
