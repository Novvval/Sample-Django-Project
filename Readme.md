### Как запустить API

1. Клонировать репозиторий:
```
git clone https://github.com/Novvval/test_project/
```
2. Создать файл .env с переменными по примеру env.example
3. Включить контейнер с базой и api:
```
docker-compose up -d
```
4. Создать superuser:
```
docker-compose run api python manage.py createsuperuser
```
5. Зайти по http://127.0.0.1:8000/