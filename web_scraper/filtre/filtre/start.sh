#!/usr/bin/bash
scrapy crawl Filtre -a urls=$(pwd)/urls1 -a rayons=$(pwd)/rayons1 -a params='{"auchan": { "nbrayons": 2, "selecteur": "nav.site-breadcrumb__nav a::text"}, "franprix": { "nbrayons": 3, "selecteur": "ul.breadcrumb.mobile-container-x.mb-6 li a::text"} }'  -O output/result1.jl &
scrapy crawl Filtre -a urls=$(pwd)/urls2 -a rayons=$(pwd)/rayons2 -a params='{"auchan": { "nbrayons": 2, "selecteur": "nav.site-breadcrumb__nav a::text"}, "franprix": { "nbrayons": 3, "selecteur": "ul.breadcrumb.mobile-container-x.mb-6 li a::text"} }'  -O output/result2.jl &
wait
cd ../../extraction
scrapy crawl -s MONGODB_URI="mongodb://nicolas:t@192.168.1.198:27017" -s MONGODB_DATABASE="Distributeur" Distributeur -a results='../filtre/filtre/output/result1.jl' &
scrapy crawl -s MONGODB_URI="mongodb://nicolas:t@192.168.1.198:27017" -s MONGODB_DATABASE="Distributeur" Distributeur -a results='../filtre/filtre/output/result2.jl'
