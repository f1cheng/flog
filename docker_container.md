docker commands

```

id = $(docker ps -a -q)

docker stop id
docker rm id
docker rmi xxx:latest

```
docker for blogs server

```




[root@VM-16-14-centos ~]# python
Python 3.9.19 (main, Jun 11 2024, 00:00:00)
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.


pip install Django
pip install django-cors-headers
pip install djangorestframework

python manage.py migrate
python manage.py runserver 0.0.0.0:9000


==========


[root@VM-16-14-centos blog]# pwd
/myhome/project/flog/blog
[root@VM-16-14-centos blog]# ls
blog  db.sqlite3  Dockerfile  manage.py  media  rest
[root@VM-16-14-centos blog]#

vi Dockerfile
==
FROM python:3.9

RUN mkdir /blogs
WORKDIR /blogs
RUN pip install Django
RUN pip install django-cors-headers
RUN pip install djangorestframework

COPY . /blogs/

EXPOSE 9000

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]

docker build -t blogs .
"
5.69 pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.

"
=>change to use pip3 in docker file
[root@VM-16-14-centos blog]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
blogs        latest    afeaa6c31df4   2 minutes ago   1.05GB
<none>       <none>    6d2b37ca80ef   2 hours ago     197MB



docker run -it -p 9000:9000 blogs
worked:via 
curl -s http://118.25.176.102:9000/decoration/cart/
http://118.25.176.102:9000/decoration/cart/

docker ps -a

^C[root@VM-16-14-centos blog]# docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                     PORTS     NAMES
d8fc6823b532   blogs     "python manage.py ru…"   2 minutes ago   Exited (0) 3 seconds ago             suspicious_kowalevski
4c393595e41b   6d2b      "cat /tmp/hello_worl…"   2 hours ago     Exited (0) 2 hours ago               exciting_edison
[root@VM-16-14-centos blog]# docker stop d8fc6823b532
d8fc6823b532
[root@VM-16-14-centos blog]# docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                      PORTS     NAMES
d8fc6823b532   blogs     "python manage.py ru…"   2 minutes ago   Exited (0) 13 seconds ago             suspicious_kowalevski
4c393595e41b   6d2b      "cat /tmp/hello_worl…"   2 hours ago     Exited (0) 2 hours ago                exciting_edison
[root@VM-16-14-centos blog]#

refer: and continue to push?
https://dockerize.io/guides/python-django-guide

============>new could test further:
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "sh", "entrypoint.sh" ]


python manage.py migrate
python manage.py runserver 0.0.0.0:9000

https://medium.com/@anshita.bhasin/a-step-by-step-guide-to-create-dockerfile-9e3744d38d11


```

To apply in backend:
```
[root@VM-16-14-centos blog]# cat Dockerfile 
FROM python:3.9

EXPOSE 9000
RUN export PIP_DEFAULT_TIMEOUT=100
#RUN pip install --upgrade pip
RUN pip3 install Django
RUN pip3 install django-cors-headers
RUN pip3 install djangorestframework

RUN mkdir /blogs
WORKDIR /blogs
COPY . /blogs/
RUN chmod +x docker_entry.sh

ENTRYPOINT [ "sh", "docker_entry.sh" ]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
[root@VM-16-14-centos blog]# cat docker_entry.sh 
echo "Blog server migrate and run"
python manage.py migrate
python manage.py runserver 0.0.0.0:9000
[root@VM-16-14-centos blog]#


==>
docker build -t blogs .
docker run -it -p 9000:9000 blogs
curl -s http://118.25.176.102:9000/decoration/cart/
```

To apply in frontend:
```  
yum install nodejs
npm install
//in frontend folder
npm run dev 
//prompt with auto injected: via curl -s http://118.25.176.102:8080/decoration/cart/

```
