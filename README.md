# Результаты тестирования
[![Coverage Status](coverage/coverage-badge.svg)](coverage/coverage-report.txt)
![Workflow Status](https://github.com/Nk3YQQ/drf-tracker-project/actions/workflows/main.yml/badge.svg)

# Установка зависимостей

Перед запуском убедитесь, что Вы установили виртуальное окружение и скачали зависимости.

## Установка зависимостей для pip
```
pip install -r requirements.txt
```

## Установка зависимостей для poetry
```
poetry install
```

# Основные команды

## Запуск compose
```
make docker-compose-run
```

## Остановка compose
```
make clean-up
```

## Запуск сервера (без compose)
```
make runserver
``` 

## Запуск тестов
``` 
make coverage
```

## Запуск celery-worker
```
make workers
```

## Запуск celery-beat
```
make celery-beat
```

При работе с проектом необходимо будет использовать API ключ stripe. 

Подробно вся информация написана здесь: https://docs.stripe.com/api. Для работы с проектом предусмотрена библиотека stripe.

Обязательно ознакомитесь с файлом .env.sample, где представлены примеры ключей для переменных окружения.