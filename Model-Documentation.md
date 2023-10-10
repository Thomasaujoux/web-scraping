# Model Documentation

## Database analysis

The algorithm I have written scrapes data from France's biggest supermarkets. Thanks to it, we can obtain information on all the food products in these stores, such as: name, price, quantity, barcode, manufacturer, claim, label, shelf life, preparation advice, nutritional values, ingredients, seasonality, origin, location and legal name.

As the sites have different structures, this section lists the various structures observed and the associated solutions.

## Security 

### Various safety features

To access the site with Scrapy, there may be various problems linked to protections on certain site :

- DataDome

Detect and mitigate bot attacks and online fraud with unrivalled accuracy and without compromise. Deployment in minutes. No impact on user experience.

- Headers 

To browse certain sites, you need to fill in headers or identify yourself. Solutions are available with Scrapy.

- Other protections

Other protections, such as query frequency, URL relocation and browsing the site without an item in the shopping cart, have been implemented on certain sites.

### Solutions

I have implemented several solutions to bypass the various security measures that can be found on sites.

The first is the user agent found in the utils.py file. I've set up a list of different user agents to bypass certain security measures, so that when the web crawler wants to send requests to different sites, it can randomly change the user agent to avoid being noticed.

The second is the obey robot.txt in the settings.py file. This option allows you to disregard what the site forbids you to scrape. In fact, the site implements security measures by warning us that certain parts are not authorized for scraping. Please note that I absolutely do not encourage you to reproduce the same thing. It's important to respect the site's authorizations if you want to scrap legally.

The last measures concern custom settings in the spyder.py file. These measures limit the flow of requests made to the site by setting long random delays and blocking cookies. This makes it harder for sites to identify whether the user is a normal user or a web-scraper. For this project, I preferred to leave long delays as the execution was done at night, which meant I was never blocked by one of these sites.

## Website Structure

### Several different types of structure

The various scraped sites have quite different structures, which prevents full automation for all sites. There are two main types of structure: static sites and dynamic sites.

A dynamic website is one that displays a different type of content each time a user visits it, because each time the website is updated. This is achieved through a combination of client-side and server-side scripts. In this way, dynamic web pages can provide users with information based on their navigation on the server.

A static website refers to a website whose content is fixed and does not change according to the characteristics of the request. In a static website, for each page of the website we want to create, we create a corresponding HTML document based on the data stored on the server. 

Static web pages integrate technologies such as HTML, JavaScript and CSS. built for this purpose. Dynamic websites, on the other hand, are also designed in HTML, JavaScript and CSS, while also using code languages such as AJAX, ASP, PERL, PHP...

### Solutions

A solution has been found to meet most requirements. Whether the site is static or dynamic, there will always be a static "Next Page" tag in the source code of the page we're analyzing, which we can retrieve from the configurations. This will enable us to find out directly what the next URL is, if any.
The solution can be found in the spyder.py file, which allows us to treat URLs differently, whether they're useless URLs or URLs enabling access to the next page. Removing URLs makes the difference between "Next Page" pages, pages relating to a product category such as "beverage" and other pages.

## URL processing

### URLs for food products

The final problem concerns the reprocessing of URLs to determine whether they are for food products or other products such as managers. In fact, we're interested in this issue because we want to end up with a database containing only food product URLs that we can use to avoid wasting time and sending too many queries.

### Solutions

The solution was to find the pattern for obtaining the URLs by looking at the URLs used to find the product. This solution resulted in a smaller list of URLs containing only useful URLs.
