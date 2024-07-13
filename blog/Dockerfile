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
