# DockerPracriceWORK1


touch Dockerfile
@shaharliviatan-web ➜ /workspaces/docker (main) $ docker pull alpine
@shaharliviatan-web ➜ /workspaces/docker (main) $ docker images
@shaharliviatan-web ➜ /workspaces/docker (main) $ docker run -i -t --name ENV1_ALPINE alpine 
@shaharliviatan-web ➜ /workspaces/docker (main) $ docker stop ENV1_ALPINE
@shaharliviatan-web ➜ /workspaces/docker (main) $ docker start ENV1_ALPINE
@shaharliviatan-web ➜ /workspaces/docker (main) $ docker exec -it ENV1_ALPINE /bin/sh