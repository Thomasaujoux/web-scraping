# web-scraping

## I) General Presentation

This repository includes the first part of my second-year internship at ENSAE (National School of Statistics and Economic Administration), which I carried out at INRAE (National Research Institute for Agriculture, Food and the Environment) over a 1-month period.

The subject is the automation and enrichment with web-crwling and web-scraping tools of a database that is maintained and fed by hand by a team of 7 people. This is the first time INRAE has used these algorithms.

WARNING: Web scraping is illegal and what was done in this project must not be reproduced. However, in the context of my internship at a research institute, Web Scraping is legal. I am therefore sharing the content of my code to help other research institutes and not to encourage illegal Web scraping.



## II) Context 

### Oqali

The Observatoire de l'Alimentation (Oqali), was created by the 2010-874 law on the modernization of agriculture and fisheries, and confirmed by the so-called "EGalim" law of October 30, 2018, and is tasked with globally monitoring the food supply of processed products on the French market by measuring changes in nutritional quality, in particular by studying the information found on product labels.

### The Oqali database

In order to monitor quality trends in the French food market, Oqali collects all the information found on the packaging of products processed in this market. To do this, it has several sources at its disposal:
- data transmitted by professionals,
- in-store visits,
- physico-chemical analyses of the nutritional composition of foods
- extraction of paid databases
- product purchases, retailer websites, etc.
The most widely used method is the transmission of data by professionals. This provides information that can be found on product labels: name, ingredients, quantities... 
The only information that is not retained is additional information that does not characterize the product: catchphrases, recipes, etc.
As part of the monitoring of Nutri-Score deployment on processed products, this information is collected by Oqali, in Excel format. Oqali has designed a two-level nomenclature to classify these products. Food families are grouped into sectors. To date, Oqali contains around thirty sectors and just over 600 families. It currently has 60,000 products already classified in this nomenclature by its teams.

### Objective

The aim of this repository is to design a Web Crawling and Web Scraping algorithm to automate the production of this database. Indeed, in the context of the current modernization of data collection, INRAE wishes to automate certain elements of database production, and also to enrich it with new elements such as price.

### Web Crawling and Web Scraping

Web crawling is defined as the use of web crawlers to index information on pages. It involves looking at the entire page and analyzes every link looking for all available information. This web crawling process generally captures general information, whereas web scraping focuses on specific data.

Web scraping is similar to web crawling in that it identifies and locates target data on web pages. The main difference is that with web scraping, we know the exact identifier of the data set, such as the structure of the HTML elements on the web page in question, from which the data is to be extracted.

## III) General information about the project

### Planning

The initial planning did not include any hard deadlines, and left room for flexibility. Here are the main stages:
- Study the Oqali database, understand how it is obtained and the different variables,
- Study of the architecture of different sites (protection, dynamic or static, URL path, available information, etc.),
- Web-scraping implementation,
- Dockerization and commissioning on INRAE server.

The foreseeable difficulties were :
- Access to different sites with protection,
- Different approach for static and dynamic sites,
- Finding a pattern to scrape the right URLs.

### Contributions

This part of the internship is a first for INRAE, which would like to automate the addition of information to its database. There was no previous work on the same theme at INRAE.

### Tools and technologies

Python is an interpreted, multi-paradigm, multi-platform programming language. It has the advantage of custom libraries, such as Scrapy, widely used in Web-scraping. The language has extensive documentation and a large community on the Internet, making it an invaluable resource in case of bugs or questions. The working environment was Visual Studio Code, a free, open source Python distribution dedicated to data science. We used a template called CookieCutter to organize the code according to the stages of our algorithm. Scrapy is a free Python library for Web-Scrawling and Web-Scraping.


### Project hierarchy

This project was carried out in two parts:
- The first involved web crawling of all Auchan and Franprix sites. The aim was to use a single URL https://www.auchan.fr/ or https://www.franprix.fr/ to retrieve all the product URLs present on the site.
- The second part concerns web scraping, in which from this list including all product URLs I'll retrieve all useful product information (Name, Price, Ingredients, Nutritional information, etc.).

Thereafter, I'll explain only the first part in detail, the second part using the same techniques and adding nothing new.



## IV) The project

### Database analysis

The algorithm I have written scrapes data from France's biggest supermarkets, such as Auchan, Franprix, Cora and Leclerc. Thanks to it, we can obtain information on all the food products in these stores, such as: name, price, quantity, barcode, manufacturer, claim, label, shelf life, preparation advice, nutritional values, ingredients, seasonality, origin, location and legal name.

As the sites have different structures, this section lists the various structures observed and the associated solutions.

### Security 

#### Various safety features

To access the site with Scrapy, there may be various problems linked to protections on certain site :
- DataDome
Detect and mitigate bot attacks and online fraud with unrivalled accuracy and without compromise. Deployment in minutes. No impact on user experience.
- Headers 
To browse certain sites, you need to fill in headers or identify yourself. Solutions are available with Scrapy.
–	Autres protections 

#### Solutions




### Taking a step back


### Conclusion

## V) How to use the project