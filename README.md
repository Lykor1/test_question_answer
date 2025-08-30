# Тестовое задание для компании "Хайталент" по реализации Question/Answer

## Описание:
Данный проект реализует возможность добавления (`localhost:8000/api/questions/`)/удаления (`localhost:8000/api/questions/{id}`)/просмотр (`localhost:8000/api/questions/`, `localhost:8000/api/questions/{id}`) вопросов, добавления (`localhost:8000/api/questions/{id}/answers/`)/удаления (`localhost:8000/api/answers/{id}`)/просмотр (`localhost:8000/api/answers/{id}`) ответов.

## Установка:
1. Клонировать репозиторий.
2. Создать .env файл по аналогии с .env.example.
3. Запустить проект командой `docker compose build` и `docker compose up`.
4. Применить миграции для БД с помощью `docker compose exec web python manage.py makemigartions` и `docker compose exec web python manage.py migrate`.
5. Перейти на `localhost:8000/api/` для работы.
6. (Опционально) Для запуска тестов применить `docker compose exec web pytest`.
