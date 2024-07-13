FROM node:18.7.0-alpine
# if centos to use yum install nodejs

EXPOSE 8080 8081

RUN mkdir /blogfe
#COPY ./package.json /blogfe/
#COPY ./package-lock.json /blogfe/

# install requirements
WORKDIR /blogfe
COPY . /blogfe/

RUN npm install --legacy-peer-deps
#RUN npm install
#RUN npm install -g npm@10.8.2
#RUN npm run dev 
CMD ["npm", "run", "dev"]

#docker build -t blogfe .
#docker run -it -p 8080:8080 blogfe
