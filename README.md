# web-scraping

## I) General Presentation

This repository includes the first part of my second-year internship at ENSAE (National School of Statistics and Economic Administration), which I carried out at INRAE (National Research Institute for Agriculture, Food and the Environment) over a 1-month period.

The subject is the automation and enrichment with web-crawling and web-scraping tools of a database that is maintained and fed by hand by a team of 7 people. This is the first time INRAE has used these algorithms.

WARNING: Web scraping is illegal and what was done in this project must not be reproduced. However, in the context of my internship at a research institute, Web Scraping is legal. I am therefore sharing the content of my code to help other research institutes and not to encourage illegal Web scraping.

[new](news)

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
- Scrap responsibly, so as not to overload the site with too much time between requests, and scrape only at night
- Different approach for static and dynamic sites,
- Time sonsuming, 
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

–	Other protections

Other protections, such as query frequency, URL relocation and browsing the site without an item in the shopping cart, have been implemented on certain sites.

#### Solutions

I have implemented several solutions to bypass the various security measures that can be found on sites.

The first is the user agent found in the utils.py file. I've set up a list of different user agents to bypass certain security measures, so that when the web crawler wants to send requests to different sites, it can randomly change the user agent to avoid being noticed.

The second is the obey robot.txt in the settings.py file. This option allows you to disregard what the site forbids you to scrape. In fact, the site implements security measures by warning us that certain parts are not authorized for scraping. Please note that I absolutely do not encourage you to reproduce the same thing. It's important to respect the site's authorizations if you want to scrap legally.

The last measures concern custom settings in the spyder.py file. These measures limit the flow of requests made to the site by setting long random delays and blocking cookies. This makes it harder for sites to identify whether the user is a normal user or a web-scraper. For this project, I preferred to leave long delays as the execution was done at night, which meant I was never blocked by one of these sites.

### Website Structure

#### Several different types of structure

The various scraped sites have quite different structures, which prevents full automation for all sites. There are two main types of structure: static sites and dynamic sites.

A dynamic website is one that displays a different type of content each time a user visits it, because each time the website is updated. This is achieved through a combination of client-side and server-side scripts. In this way, dynamic web pages can provide users with information based on their navigation on the server.

A static website refers to a website whose content is fixed and does not change according to the characteristics of the request. In a static website, for each page of the website we want to create, we create a corresponding HTML document based on the data stored on the server. 

Static web pages integrate technologies such as HTML, JavaScript and CSS. built for this purpose. Dynamic websites, on the other hand, are also designed in HTML, JavaScript and CSS, while also using code languages such as AJAX, ASP, PERL, PHP...

#### Solutions

A solution has been found to meet most requirements. Whether the site is static or dynamic, there will always be a static "Next Page" tag in the source code of the page we're analyzing, which we can retrieve from the configurations. This will enable us to find out directly what the next URL is, if any.
The solution can be found in the spyder.py file, which allows us to treat URLs differently, whether they're useless URLs or URLs enabling access to the next page. Removing URLs makes the difference between "Next Page" pages, pages relating to a product category such as "beverage" and other pages.

### URL processing

#### URLs for food products

The final problem concerns the reprocessing of URLs to determine whether they are for food products or other products such as managers. In fact, we're interested in this issue because we want to end up with a database containing only food product URLs that we can use to avoid wasting time and sending too many queries.

#### Solutions

The solution was to find the pattern for obtaining the URLs by looking at the URLs used to find the product. This solution resulted in a smaller list of URLs containing only useful URLs.


### Conclusion

This project enabled us to scrape the entire Auchan and Franprix sites, and is replicable to other major chains by changing certain parts of the code.
Here's a table showing the different results obtained:

|  | #Total number of urls   | #URLs retrieved with data   | #Missing urls   | #Recovery rates   | 
| :---:   | :---: | :---: | :---: | :---: |
| Auchan | 24005   | 20334   | 3671   | 84,71%   |
| Franprix | 13626   | 9126   | 4500   | 66,97%   |

We can see that the recovery rate isn't 100%, due to the fact that some URLs have been moved or don't contain all the information, so Scrapy can't scrape them.


## V) How to use the project

### To select Auchan or Franprix

You need to modify the .env file in which you can comment out the Auchan part or the Franprix part, depending on the site you want to scrape.

### Via Docker

Image construction:

	- docker build --file web_crawler/DockerFile -t web_crawler .

Docker container creation with:
	
	- docker run --name auchan -v [path_local]:/crawler/log  web_crawler ./start_.sh

### Via sources

To run the program :

	- place in the first url branch (ex : cd .//src/web_crawler/url)
	- Enter : scrapy crawl url --logfile laph.log -o laph.jl -t jsonlines

### Wiki

To understand better how to use the project, you can see the Wiki

## VI) Future of the project

### Idea to improve the project

Security :
The security of the different websites can change anytime and there are many solutions to bypass security which can be find online.

The headers :
The headers can be a big issue in the future because some sites in order to be scraped require to put headers with the localisation and other informations.
