# LotteryMatching
 
 
## Table of Centents
- [Prerequisites](#prerequisites)
- [Local Deployment](#local-deployment)

## Prerequisites
1. Install
- python3.9
  https://www.python.org/downloads/
- docker
  https://docs.docker.com/get-docker/
- docker-compose
  https://docs.docker.com/compose/install/
- postgresql13
  - **Windows**
    https://www.postgresql.org/download/windows/
- gcloud CLI
  https://cloud.google.com/sdk/docs/install

---

## Local Deployment
(If deploy on linux, see change at the bottom )
1. Get Project 
  - ```https://github.com/SirisakUnknowss/LotteryMatching2022.git```
  - ``` cd Arkarus ```
2. See [Setup container ip](#setup-container-ip)
  
3. Prepare web service to chosen \<IP\>
  - ``` docker-compose up -d ```
  - Stop web service
    ``` docker-compose stop ```
  
4. See [Setup Postgres](#setup-postgres)

5. Start web service
  ``` docker-compose up -d ```

6. Run Migrations
  - ``` docker-compose exec web sh -c "python manage.py makemigrations --noinput" ```
  - ``` docker-compose exec web sh -c "python manage.py migrate --noinput" ```
7. Create superuser
  - ``` docker-compose exec web sh -c "python manage.py createsuperuser --noinput" ```

8. Delete Data

   - ``` sudo docker-compose -f docker-compose-prod.yaml exec lottery-web sh -c "python manage.py deleteData --name shop" ```
   - ``` sudo docker-compose -f docker-compose-prod.yaml exec lottery-web sh -c "python manage.py deleteData --name numberLottery" ```
8. go to http://localhost:8000

> PS. admin page: http://localhost:8000/admin

---
