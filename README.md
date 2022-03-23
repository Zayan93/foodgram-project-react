# Социальная сеть для любителей Кулинарии: Foodgram (foodgram-project-react)


## Описание
«Продуктовый помощник» (Проект Яндекс.Практикум) Сайт является - базой кулинарных рецептов. Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в txt формате. Также присутствует файл docker-compose, позволяющий , быстро развернуть контейнер базы данных (PostgreSQL), контейнер проекта django + gunicorn и контейнер nginx

http://130.193.53.204 


Подготовка и запуск проекта
Склонировать репозиторий на локальную машину:
git clone https://github.com/zayan93/foodgram-project-react
Для работы с удаленным сервером (на ubuntu):
Выполните вход на свой удаленный сервер

Установите docker на сервер:

sudo apt install docker.io 
Установите docker-compose на сервер:
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
Локально отредактируйте файл infra/nginx.conf и в строке server_name впишите свой IP
Скопируйте файлы docker-compose.yml и nginx.conf из директории infra на сервер:
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
Cоздайте .env файл и впишите:

DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ проекта django>

