docker stop poxterbot
docker rm poxterbot
# cd [PoxterBot directory]
docker-compose build
docker run --name poxterbot --restart always poxterbot