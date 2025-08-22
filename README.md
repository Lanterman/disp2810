# DISP2810 - full project


### Launch of the project

#### 1) Clone repository
```
git clone https://github.com/Lanterman/disp2810.git
```
#### 2) Create and run docker-compose
```
docker-compose up -d --build
```
##### 2.1) To create a superuser, run the following instruction:
```
docker exec -it <backend_container_ID> python manage.py createsuperuser
```

#### 3) Follow the link in the browser:
```
http://0.0.0.0:8000/
```
