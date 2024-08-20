docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -q) -f
docker volume rm $(docker volume ls -q) -f
docker network prune -f
docker system prune -a -f --volumes
