# Barter Platform — Django веб-приложение для обмена вещами

Платформа для размещения объявлений и предложений на обмен товарами между пользователями. Поддерживает как HTML-интерфейс, так и REST API с авто-документацией.

---

## Возможности

- Регистрация и авторизация пользователей
- Создание, редактирование и удаление объявлений
- Поиск и фильтрация объявлений по ключевым словам, категории и состоянию
- Отправка и обработка предложений на обмен
- Веб-интерфейс и REST API (с использованием Django REST Framework + Swagger UI)
- Покрытие тестами базовой функциональности

---

## Технологии

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite (по умолчанию, можно использовать PostgreSQL)
- Bootstrap (в шаблонах, опционально)
- drf-spectacular (для автодокументации API)

---

## Установка и запуск

# Клонируйте репозиторий
    git clone https://github.com/oberonmaster/TestTaskEM
    cd TestTaskEM

# Создайте виртуальное окружение
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Установите зависимости
    pip install -r requirements.txt

# Выполните миграции
    python manage.py migrate

# Запустите сервер
    python manage.py runserver 

---

## Пользовательский интерфейс

- Главная: `/` — список объявлений
- Создание объявления: `/ads/create/`
- Вход / Регистрация: `/login/`, `/register/`
- Создание и просмотр предложений: `/proposals/`

---

## Запуск тестов

    python manage.py test ads

---

## REST API

Документация доступна по адресу:

- Swagger UI: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
- OpenAPI JSON: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

Доступные ресурсы:

- `GET /api/ads/` — список объявлений с фильтрацией
- `POST /api/ads/` — создание объявления
- `PUT /api/ads/{id}/` — обновление
- `DELETE /api/ads/{id}/` — удаление

- `POST /api/proposals/` — отправка предложения обмена
- `PUT /api/proposals/{id}/` — обновление статуса
- `GET /api/proposals/` — фильтрация по отправителю/получателю/статусу

---

## Структура проекта

    barter_platform/
    ├── ads/                # Основное приложение
    │   ├── models.py       # Модели Ad и ExchangeProposal
    │   ├── views.py        # Класс-based views для CRUD
    │   ├── serializers.py  # DRF сериализаторы
    │   ├── forms.py        # Django формы
    │   ├── urls.py         # Маршруты приложения
    │   ├── templates/      # HTML-шаблоны
    │   ├── tests.py        # Unit-тесты
    │   └── api/            # API views
    │
    ├── barter_platform/    # Конфигурация проекта
    ├── manage.py
    └── requirements.txt

---

## Автор

Разработано в рамках тестового задания.
