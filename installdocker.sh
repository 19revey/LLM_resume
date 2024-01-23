#optinal

sudo apt-get update -y

sudo apt-get upgrade -y

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh -y

sudo usermod -aG docker ubuntu 

newgrp docker