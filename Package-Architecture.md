# Package architecture

## Architecture

    ├── Dockerfile <- Docker implementation
    ├── requirements.txt
    ├── traitement.py <- Post-processing of the database
    └── url/
        ├── .env <- Where we put the different variables in order to change the website to scrap
        ├── scrapy.cfg
        ├── start.sh <- Command line to start the package
        └── url/
            ├── items.py
            ├── middlewares.py
            ├── pipelines.py <- To process the data
            ├── settings.py
            ├── spiders/
            │   └── spyder.py <- The spyder to crawl the data
            └── utils.py <- To change user agent

## How is it working ?

To better understand how the package works, you should first read [the Scrapy documentation](https://docs.scrapy.org/en/latest/intro/overview.html).

The operation is summarised in the *rules* variable of the **myCrawler** class. 

1. The package will first make a request on the initial page to get the information contained on it.

2. Given that there are no product links on this page, nor any links to access pages 2, 3, etc., the algorithm will only process the product links. The algorithm will only process links relating to the food aisles. 

3. It will then make a request to scrape these new pages.

3. a. Either it's a product URL and so the class will use the *callback* called *parse_item* to store the information. 

3. b. The second possibility is that it is a URL for page number two and so the process will continue.

4. The package only stops when there are no URLs left to process in the domain name in which it is authorised.