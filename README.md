# Data-WebTechniques
Masters Project for the Subject of DWT. We have made a Web app which helps us in selecting different dishes. 

## Setup Environment
For setting up environment for this project we need to have some Pre-requisites
### Pre-Requisites
1. Docker needs to be installed in you machine. Installation for docker is found on offical website https://docs.docker.com/install/
2. Docker compose needs to be installed
  pip install docker-compose

After that we need to download the code from this repository enter the project and run the following commands:

**git clone https://github.com/Deltaidiots/Data-WebTechniques.git**
<br />
**cd Data-WebTechniques**
<br />
**docker-compose build**
<br />
**docker-compose up -d**
<br />

Now you **App** will be running on http://localhost
and the **API** can be accessed on http://localhost/81

## Migrating Data to Database
In order to migrate the data manually run the following link in browser respectively 

1. http://localhost/crawl_portofino
2. http://localhost/crawl_asiaresturant
3. http://localhost/crawl_amano
4. http://localhost/crawl_asiaresturant
5. http://localhost/crawl_langosch
6. http://localhost/crawl_pdf
