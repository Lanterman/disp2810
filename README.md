# DISP2810 - full project


### Запуск проекта

#### 1) Клоринуйте репозиторий
```
git clone https://github.com/Lanterman/disp2810.git
```
#### 2) Войдите в директорию
```
cd disp2810
```
#### 3) Создайте и запустите docker-compose
```
sudo docker-compose up --build
```
#### 4) Перейдите по ссылке в браузере:
```
http://0.0.0.0:8000/
```

P.S.
#### Выключение
```
sudo docker-compose down --volumes
```

P.S.S.
Знаю, что виртуалки (.env и .env.dev) надо скрывать, но сделано это было целенаправленно для упрощения.
