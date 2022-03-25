#!/bin/bash

sudo yum update

sudo yum install git -y

git clone https://github.com/Algerdi/instagram.git

cd instagram

sudo yum install docker -y

sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

sudo service docker start

sudo docker-compose up
