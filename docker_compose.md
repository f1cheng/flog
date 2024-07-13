
To refer: vue depends on django

```

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
cd /myhome/project/flog/
[root@VM-16-14-centos flog]# ls
blog  docker-compose.yml  fe  install2.md  install.md  README.md  run_py_server.sh  run_vue.sh

docker compose up -d
then in web: http://118.25.176.102:8080/
//////////////////////////////////////////
[root@VM-16-14-centos flog]# docker compose up -d
[+] Building 21.4s (24/24) FINISHED                                                                                                                                                                                           docker:default
 => [server internal] load build definition from Dockerfile                                                                                                                                                                             0.0s
 => => transferring dockerfile: 407B                                                                                                                                                                                                    0.0s
 => [server internal] load metadata for docker.io/library/python:3.9                                                                                                                                                                    0.7s
 => [server internal] load .dockerignore                                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                                         0.0s
 => [server 1/9] FROM docker.io/library/python:3.9@sha256:47d6f16aa0de11f2748c73e7af8d40eaf44146c6dc059b1d0aa1f917f8c5cc58                                                                                                              0.0s
 => [server internal] load build context                                                                                                                                                                                                4.6s
 => => transferring context: 7.81MB                                                                                                                                                                                                     3.7s
 => CACHED [server 2/9] RUN export PIP_DEFAULT_TIMEOUT=100                                                                                                                                                                              0.0s
 => CACHED [server 3/9] RUN pip3 install Django                                                                                                                                                                                         0.0s
 => CACHED [server 4/9] RUN pip3 install django-cors-headers                                                                                                                                                                            0.0s
 => CACHED [server 5/9] RUN pip3 install djangorestframework                                                                                                                                                                            0.0s
 => CACHED [server 6/9] RUN mkdir /blogs                                                                                                                                                                                                0.0s
 => CACHED [server 7/9] WORKDIR /blogs                                                                                                                                                                                                  0.0s
 => CACHED [server 8/9] COPY . /blogs/                                                                                                                                                                                                  0.0s
 => CACHED [server 9/9] RUN chmod +x docker_entry.sh                                                                                                                                                                                    0.0s
 => [server] exporting to image                                                                                                                                                                                                         0.0s
 => => exporting layers                                                                                                                                                                                                                 0.0s
 => => writing image sha256:e293ed6238b02fd7bcfe2d4aa133e2e48550286b361b86104ce2f132248ddb48                                                                                                                                            0.0s
 => => naming to docker.io/library/flog-server                                                                                                                                                                                          0.0s
 => [web internal] load build definition from Dockerfile                                                                                                                                                                                0.0s
 => => transferring dockerfile: 450B                                                                                                                                                                                                    0.0s
 => [web internal] load metadata for docker.io/library/node:18.7.0-alpine                                                                                                                                                               0.7s
 => [web internal] load .dockerignore                                                                                                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                                                                                                         0.0s
 => [web 1/5] FROM docker.io/library/node:18.7.0-alpine@sha256:02a5466bd5abde6cde29c16d83e2f5a10eec11c8dcefa667a2c9f88a7fa8b0b3                                                                                                         0.0s
 => [web internal] load build context                                                                                                                                                                                                  14.7s
 => => transferring context: 192.71MB                                                                                                                                                                                                  14.7s
 => CACHED [web 2/5] RUN mkdir /blogfe                                                                                                                                                                                                  0.0s
 => CACHED [web 3/5] WORKDIR /blogfe                                                                                                                                                                                                    0.0s
 => CACHED [web 4/5] COPY . /blogfe/                                                                                                                                                                                                    0.0s
 => CACHED [web 5/5] RUN npm install --legacy-peer-deps                                                                                                                                                                                 0.0s
 => [web] exporting to image                                                                                                                                                                                                            0.1s
 => => exporting layers                                                                                                                                                                                                                 0.0s
 => => writing image sha256:056620c1eb901ed5018b8a43437ac9e08fe2ff0fb1c67327024464895412b125                                                                                                                                            0.0s
 => => naming to docker.io/library/flog-web                                                                                                                                                                                             0.0s
[+] Running 2/2
 ✔ Container flog-server-1  Started                                                                                                                                                                                                     1.2s
 ✔ Container flog-web-1     Started                                                                                                                                                                                                     1.1s
[root@VM-16-14-centos flog]# pwd


[root@VM-16-14-centos flog]# docker compose ps -a
NAME            IMAGE         COMMAND                  SERVICE   CREATED         STATUS         PORTS
flog-server-1   flog-server   "sh docker_entry.sh"     server    2 minutes ago   Up 2 minutes   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp
flog-web-1      flog-web      "docker-entrypoint.s…"   web       2 minutes ago   Up 2 minutes   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 8081/tcp
[root@VM-16-14-centos flog]# docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                                 NAMES
8d50e2589303   flog-web      "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 8081/tcp   flog-web-1
7cb066418d3e   flog-server   "sh docker_entry.sh"     2 minutes ago   Up 2 minutes   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp             flog-server-1
[root@VM-16-14-centos flog]# docker images
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
flog-web      latest    056620c1eb90   42 minutes ago   377MB
flog-server   latest    e293ed6238b0   25 hours ago     1.05GB
[root@VM-16-14-centos flog]#


```


```



https://www.reddit.com/r/django/comments/uwc1bq/using_django_vue_in_docker_for_development/?rdt=47678


#docker-compose.yml
version: "3.9"

services:
db:
image: postgres
environment:
   - POSTGRES_NAME=postgres
   - POSTGRES_USER=postgres
   - POSTGRES_PASSWORD=postgres
server:
 build: server/
 command: python manage.py runserver 0.0.0.0:8000
 ports:
   - "8000:8000"
environment:
   - POSTGRES_NAME=postgres
   - POSTGRES_USER=postgres
   - POSTGRES_PASSWORD=postgres
 depends_on:
   - db
client:
  build: client/
  command: npm run serve
  ports:
    - '8081:8080'
  depends_on:
    - server

#server django Dockerfile
# pull the official base image
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD="admin"

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000


CMD ["python", "manage.py", "runserver"]

#client vue Dockerfile
FROM node:14.17.5 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN npm run build
EXPOSE 8080
CMD [ "npm", "run", "serve" ]

https://stackoverflow.com/questions/53345283/docker-container-set-up-for-django-vuejs






# base image
FROM node:10.15.0

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json
RUN npm install
RUN npm install -g @vue/cli
# start app
CMD ["npm", "run", "serve"]




FROM node:lts-alpine
# install simple http server for serving static content
RUN npm install -g http-server
# make the 'app' folder the current working directory
WORKDIR /app
# copy 'package.json' to install dependencies
COPY package*.json ./
# install dependencies
RUN npm install
# copy files and folders to the current working directory (i.e. 'app' folder)
COPY . .
# build app for production with minification
RUN npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]


docker-compose file could be as simple as

version: "3.7"

services:
  vue-app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: vue-app
    restart: always
    ports:
      - "8080:8080"
    networks:
      - vue-network
networks:
  vue-network:
    driver: bridge

https://mherman.org/blog/dockerizing-a-vue-app/



Project structure:

.
├── compose.yaml
├── README.md
└── vuejs
    ├── Dockerfile
    └── ...
compose.yaml

services:
  web:
    build: vuejs
    ports:
    - 80:8080
    volumes:
    - ./vuejs:/project
    - /project/node_modules



$ docker compose up -d
Creating network "vuejs_default" with the default driver
Building web
Step 1/8 : FROM node:13.10.1-alpine
...
Successfully tagged vuejs_web:latest
WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating vuejs_web_1 ... done
```
