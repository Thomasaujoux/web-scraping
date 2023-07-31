#!/bin/bash
scrapy crawl url --logfile /crawler/log/laph.log -o /crawler/log/laph.jl -t jsonlines
