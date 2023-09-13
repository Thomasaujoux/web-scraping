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
