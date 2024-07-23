# Результаты тестирования
![Workflow Status](https://github.com/Nk3YQQ/drf-online-education/actions/workflows/main.yml/badge.svg)
[![Coverage Status](coverage/coverage-badge.svg)](coverage/coverage-report.txt)

# Структура проекта
```
dfr-online-education/
|—— config/ # Настройки проекта
    |—— __init__.py
    |—— asgi.py
    |—— settings.py
    |—— urls.py
    |—— wsgi.py
|—— coverage/ # Результаты тестрования
|—— fixtures/ # Фикстуры для проекта
|—— payment/ # Приложение оплаты
    |—— management/
    |—— migrations/
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— models.py
    |—— serializers.py
    |—— services.py
    |—— tests.py
    |—— urls.py
    |—— views.py
|—— service/ # Приложение онлайн-сервиса
    |—— migrations/
    |—— tests/
        |—— __init__.py
        |—— test_course.py
        |—— test_lesson.py
        |—— test_subscription.py
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— models.py
    |—— paginators.py
    |—— serializers.py
    |—— services.py
    |—— tasks.py
    |—— urls.py
    |—— views.py
|—— users/ # Приложение пользователей
    |—— management/
    |—— migartions/
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— models.py
    |—— permissions.py
    |—— serializers.py
    |—— tasks.py
    |—— tests.py
    |—— urls.py
    |—— views.py
|—— .dockerignore
|—— .env.sample
|—— .flake8
|—— .gitignore
|—— docker-compose.yml
|—— Dockerfile
|—— LICENSE
|—— Makefile
|—— manage.py
|—— poetry.lock
|—— pyproject.toml
|—— README.md
|—— requirements.txt
```

# Результаты работы:
- ### Реализован CRUD для платежа, курса, урока и пользователей
- ### Создан механизм для отправки уведомлений и периодических задач с Celery и Redis
- ### Интегрировано API сервиса обработки платежей Stripe
- ### Реализована фильтрация и пагинация для обработчиков
- ### Внедрена встроенная административная панель и написаны команды для создания админа и модератора
- ### Разработан механизм аутентификации и авторизации с помощью JWT
- ### Сборка и запуска приложения осуществляется с помощью Docker
- ### Написаны тесты для API 

# Основной стек проекта:
- ### Python 3.10
- ### Django 4.2
- ### Django REST Framework 3.15
- ### PostgreSQL 11
- ### Django ORM
- ### Redis
- ### Celery
- ### Stripe
- ### Docker
- ### GitHub Actions (CI)

# Как пользоваться проектом

## 1) Скопируйте проект на Ваш компьютер
```
git clone git@github.com:Nk3YQQ/drf-online-education.git
```

## 2) Добавьте файл .env для переменных окружения
Чтобы запустить проект, понадобятся переменные окружения, которые необходимо добавить в созданный Вами .env файл.

Пример переменных окружения необходимо взять из файла .env.sample

## 3) Запустите проект

Запуск проекта
```
make run
```

Остановка проекта
```
make stop
```
