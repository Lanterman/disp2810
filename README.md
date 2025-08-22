# DISP2810 - full project


### Launch of the project

#### 1) Clone repositories
```
git clone https://github.com/Lanterman/seabattle_backend.git
git clone https://github.com/Lanterman/seabattle_frontend.git
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
