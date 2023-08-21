# Ne sert que pour faire des tests
docker build --file docker/Dockerfile -t webscraping/scrap:1.0 .
docker run --name scrap -d webscraping/scrap:1.0
docker exec -it scrap ./start.sh
docker stop scrap
docker container rm scrap