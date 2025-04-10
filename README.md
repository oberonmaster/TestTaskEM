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

```bash
# Клонируйте репозиторий
git clone https://github.com/your-username/barter-platform.git
cd barter-platform

# Создайте виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt

# Выполните миграции
python manage.py migrate

# Запустите сервер
python manage.py runserver
