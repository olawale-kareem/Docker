# 🚀  1. What is Docker?
# ►  What is a container and what problems does it solve?
# ►  Container repository - where do containers live?

# 🚀  2. What is a Container technically
# ►  What is a container technically? (layers of images)
# ►  Demo part (docker hub and run a docker container locally)

# 🚀  3. Docker vs Virtual Machine

# operating system have 2 layers
# 1. Application layer : built on the kernel
# 2. Kernel layer: talks to the hardware
# 3. Hardware


# docker provides the application layer alone and uses the host kernel
# that means each docker image runs on specific host
# to run a docker image on a completely different host, let say linux docker image on windows
# you will neeed to download dockertool box to tak to the kernel


# 🚀  4. Docker Installation
# ►  Before Installing Docker - prerequisites
# ►  Install docker on Mac, Windows, Linux

# ❗️ Note: Docker Toolbox has been deprecated. Please use Docker Desktop instead. See for Mac (https://docs.docker.com/docker-for-mac/) and for Windows (https://docs.docker.com/docker-for-wi...).

# 🚀  5. Main Docker Commands
# ►  docker pull, docker run, docker ps, docker stop, docker start, port mapping

# the difference between a container and an image
# a container is the running enviroment for the image
# it houses the application, config files, file system and application image
# it is binded to port 5000, where it communicates with the files inside of it
# it operates a virtual file system


# CONTAINER port and HOST port
# you can have multiple docker container with the same server but must be binded with different host server
# docker run -p6000:6379 -d redis  # run the redis container binded to port 6000 and run in detached mode
# docker run -p6001:6379 -d redis:4.0  # run the redis:4.0 container binded to port 6001 and run in detached mode

# 🚀  6. Debugging a Container
# ►  docker logs, docker exec -it

# 🚀  7. Demo Project Overview - Docker in Practice (Nodejs App with MongoDB and MongoExpress UI)

# workflow with docker
# development, CI:CD, deployment

# 🚀  8. Developing with Containers 
# ►  JavaScript App (HTML, JavaScript Frontend, Node.js Backend)
# ►  MongoDB and Mongo Express Set-Up with Docker
# ►  Docker Network concept and demo

# 🚀  9. Docker Compose - Running multiple services
# ►  What is Docker Compose?
# ►  How to use it - Create the Docker Compose File
# ►  Docker Networking in Docker Compose

# 🚀  10. Dockerfile - Building our own Docker Image
# ►  What is a Dockerfile?
# ►  Create the Dockerfile
# ►  Build an image with Dockerfile

# 🚀  11. Private Docker Repository - Pushing our built Docker Image into a private Registry on AWS
# ►  Private Repository on AWS ECR
# ►  docker login
# ►  docker tag
# ►  Push Docker Image to the Private Repo

# 🚀  12. Deploy our containerized application

# 🚀  13. Docker Volumes - Persist data in Docker
# ►  When do we need Docker Volumes?
# ►  What is Docker Volumes?
# ►  Docker Volumes Types

# 🚀  14. Volumes Demo - Configure persistence for our demo project



