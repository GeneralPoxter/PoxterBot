if [ "$(docker ps -a | grep poxterbot)" ]; then
    docker stop poxterbot
    docker rm poxterbot
fi
# cd [PoxterBot directory]
docker-compose build
docker run --name poxterbot --restart always poxterbot
