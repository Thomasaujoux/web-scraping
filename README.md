# Automated retrieval of information on food products using web-scraping

<p align="center">
<img src='pictures/Capture d’écran 2023-09-14 112231.png' alt="banner"></img>
</p>

## I) General Presentation

This repository includes the first part of my second-year internship at ENSAE (National School of Statistics and Economic Administration), which I carried out at INRAE (National Research Institute for Agriculture, Food and the Environment) over a 1-month period.

The subject is the automation and enrichment with web-crawling and web-scraping tools of a database that is maintained and fed by hand by a team of 7 people. This is the first time INRAE has used these algorithms.

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


## IV) Project hierarchy

This project was carried out in two parts:
- The first involved web crawling of all sites. 
- The second part concerns web scraping, in which from this list including all product URLs I'll retrieve all useful product information (Name, Price, Ingredients, Nutritional information, etc.).

Thereafter, I'll explain only the first part in detail, the second part using the same techniques and adding nothing new.

[This document](https://github.com/Thomasaujoux/web-scraping/blob/main/Package-Architecture.md) explains the project hierarchy in more detail

## IV) The project

[This document](https://github.com/Thomasaujoux/web-scraping/blob/main/Model-Documentation.md) explains the different concepts you need to know before modifying the project.

## V) How to use the project

### Getting to know the Scrapy package

The first thing to do is find out about the Scrapy python library, on which most of the project is based. You should familiarise yourself with small projects and read the documentation carefully.

### How to change the .env file?

You need to modify the .env file in which you can comment out, depending on the site you want to scrape.

*PAGE* = This variable is used to filter URLs and determine whether the URL is page number 2, 3, etc. The programme treats this type of page differently to others, which allows efficient management of data processing. The algorithm will directly take the information from this page and look to see if there is a next page or not. To change this variable, all you have to do is look at the URLs of the site you want to scrape to see how the term page is written to indicate which page you are on. This variable will probably remain the same for the different sites.

*PRODUCTS* = This variable is used to filter URLs and determine whether the URL is a food product. The programme treats this type of page differently to others, which allows efficient data processing management. The algorithm will directly take the information from this page and will not process the URLs present on this page. To change this variable, all you have to do is look at the URLs of the site you want to scrape to see how the term is written to indicate that you are on a product URL. This variable will probably change for the different sites.

*ALLOWEDDOMAINS* = Cette variable correspond au nom de domaine du site que vous voulez scraper. Elle va donc changer en fonction du site et est facilement remplacable.

*STARTURLS* = *BASEURL* = This variable corresponds to the URL at which you want to start scraping. The two variables are not necessarily equal depending on the context, but it is good practice to set the two variables equal. A good way of using this variable is to position it on the first URL of the site, i.e. the main URL because the other URL will be filtered thanks toother variables.

*RAYONS* = This variable is used to filter URLs and determine whether the URL is a radius. The program treats this type of page differently to others, which allows efficient management of data processing. The algorithm will only process radius URLs and for data storage. In fact, in terms of data management, the algorithm will only decide to keep the URLs present on this type of page. To change this variable, all you have to do is look at the URLs of the site you want to scrape to see how the term is written to indicate that you are on a spoke URL. This variable will probably change for the different sites.

*TAGS* = This variable is used to identify patterns in the HTML code that can be used to determine whether the information is a URL. To do this, it is necessary to identify tags for both food products and links for category pages. A simple way of using it is to find the tag that concerns all the URLs on the site and the algorithm will process the rest by itself.

### How to use this project locally?

1. Download this repository

2. Change the .env file by passing into commentary the food store you don't want to scrape

3. Go to the folder of the project called "web-scraping"

4. Run the image construction :

```bash
docker build --file web_crawler/DockerFile -t web_crawler .
```

5. Create the container :

```bash
docker run --name [name_of_the_food_store] -v [path_local]:/crawler/log  web_crawler ./start_.sh
```

6. End the run of the container

7. Look in the **.log** and **.jl** file to see the result.

### Wiki

To understand better how to use the project, you can see [the Wiki](https://github.com/Thomasaujoux/web-scraping/wiki).

## V) Conclusion

This project enabled us to scrape the entire sites, and is replicable to other major chains by changing certain parts of the code.
Here's a table showing the different results obtained:

|  | Total number of urls   | URLs retrieved with data   | Missing urls   | Recovery rates   | 
| :---:   | :---: | :---: | :---: | :---: |
| Site 1 | 24005   | 20334   | 3671   | 84,71%   |
| Site 2 | 13626   | 9126   | 4500   | 66,97%   |

We can see that the recovery rate isn't 100%, due to the fact that some URLs have been moved or don't contain all the information, so Scrapy can't scrape them.

We will now analyse the statistics of one company, here it will be Site 1



We can describe these results by making some interesting observations. Firstly, the fact that there is a huge amount of data compared to the number of sectors to be classified, which will enable us to obtain statistically justifiable results. Another problem is that the number of products is not at all the same depending on the sector, which poses a problem of imbalanced dataset. We will come back to these different elements later in the report.

## VI) Future of the project

### Idea to improve the project

Security :
The security of the different websites can change anytime and there are many solutions to bypass security which can be find online.

The headers :
The headers can be a big issue in the future because some sites in order to be scraped require to put headers with the localisation and other informations.
