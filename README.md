# instagram
# How do develop
Install Docker and Docker Compose and run `docker-compose up` from project root
# Branching workflow
https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
https://0xc0d1.com/blog/git-stack/

# Useful dev tools
https://github.com/pyenv/pyenv
https://github.com/nvm-sh/nvm

https://python-poetry.org/
# Manual deployment
- [Reference](https://medium.com/@umairnadeem/deploy-to-aws-using-docker-compose-simple-210d71f43e67)
---
## Setup
- [Got to AWS EC2 console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1)
- Create a micro EC2 instance
- Create a new default VPC
- Download the key-pair file (*.pem)
### On your local machine
- `cd {project_root}`
- `mv ~/Downloads/mypair.pem .`
- `chmod 400 mypair.pem`
- `zip -r instagram.zip .`
- `scp -r -i mypair.pem ./instagram.zip ec2-user@54.173.189.173:~/`
- `ssh -i mypair.pem ec2-user@54.173.189.173`
### On the EC2 instance
- `unzip instagram.zip -d instagram`
- `cd instagram`
- `sudo yum update`
- `sudo yum install docker`
- ```sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null```
- `sudo chmod +x /usr/local/bin/docker-compose`
- `sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`
- `sudo service docker start`
- `sudo docker-compose up`
---
## Resource sharing
- Based on the docs it looks like it's not possible to share EC2 instances (https://docs.aws.amazon.com/ram/latest/userguide/shareable.html)
---
## Teardown
- There are several options:
    - https://stackoverflow.com/questions/44391817/is-there-a-way-to-list-all-resources-in-aws
    - https://github.com/rebuy-de/aws-nuke
