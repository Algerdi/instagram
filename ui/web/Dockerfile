# pull official base image
FROM node:16.14.0-alpine

# set working directory
WORKDIR /ui/web

# add `/app/node_modules/.bin` to $PATH
ENV PATH /ui/web/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# add app
COPY . .
