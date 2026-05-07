# Yatube API

REST API для социальной сети Yatube, позволяющая пользователям создавать посты, комментировать их, подписываться на других пользователей и организовывать контент по группам.

## Описание

Yatube API предоставляет полнофункциональный REST API для управления постами, комментариями, подписками и группами. API использует JWT-токены для аутентификации и поддерживает различные уровни доступа для аутентифицированных и неаутентифицированных пользователей.

### Основные возможности

- **Управление постами**: создание, чтение, обновление и удаление постов
- **Комментарии**: добавление и управление комментариями к постам
- **Подписки**: подписка на других пользователей и просмотр своих подписок
- **Группы**: организация постов по группам
- **Аутентификация**: JWT-токены для безопасного доступа к API
- **Фильтрация и поиск**: поиск по постам и подпискам

## Установка

### Требования

- Python 3.8+
- Django 3.2.16
- Django REST Framework 3.12.4
- djangorestframework-simplejwt 4.7.2

### Шаги установки

1. **Клонируйте репозиторий**
   ```bash
   git clone <repository-url>
   cd api-final-yatube-ad
   ```

2. **Создайте виртуальное окружение**
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции**
   ```bash
   cd yatube_api
   python manage.py migrate
   ```

5. **Создайте суперпользователя (опционально)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер разработки**
   ```bash
   python manage.py runserver
   ```

API будет доступен по адресу `http://127.0.0.1:8000/api/v1/`

## Примеры использования

### Аутентификация

#### Получение JWT-токена

```bash
curl -X POST http://127.0.0.1:8000/api/v1/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "password"}'
```

**Ответ:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Обновление токена

```bash
curl -X POST http://127.0.0.1:8000/api/v1/jwt/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'
```

### Посты

#### Получить список всех постов

```bash
curl -X GET http://127.0.0.1:8000/api/v1/posts/
```

**Ответ:**
```json
[
  {
    "id": 1,
    "text": "Мой первый пост",
    "author": "username",
    "image": null,
    "group": 1,
    "pub_date": "2024-01-15T10:30:00Z"
  }
]
```

#### Создать новый пост

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Новый пост",
    "group": 1
  }'
```

#### Получить пост по ID

```bash
curl -X GET http://127.0.0.1:8000/api/v1/posts/1/
```

#### Обновить пост

```bash
curl -X PUT http://127.0.0.1:8000/api/v1/posts/1/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Обновленный текст"}'
```

#### Удалить пост

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/posts/1/ \
  -H "Authorization: Bearer your_access_token"
```

### Комментарии

#### Получить комментарии к посту

```bash
curl -X GET http://127.0.0.1:8000/api/v1/posts/1/comments/
```

#### Добавить комментарий

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/1/comments/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Отличный пост!"}'
```

#### Обновить комментарий

```bash
curl -X PUT http://127.0.0.1:8000/api/v1/posts/1/comments/1/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Обновленный комментарий"}'
```

#### Удалить комментарий

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/posts/1/comments/1/ \
  -H "Authorization: Bearer your_access_token"
```

### Подписки

#### Получить список подписок текущего пользователя

```bash
curl -X GET http://127.0.0.1:8000/api/v1/follow/ \
  -H "Authorization: Bearer your_access_token"
```

**Ответ:**
```json
[
  {
    "user": "current_user",
    "following": "other_user"
  }
]
```

#### Подписаться на пользователя

```bash
curl -X POST http://127.0.0.1:8000/api/v1/follow/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"following": "username"}'
```

#### Поиск подписок

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/follow/?search=username" \
  -H "Authorization: Bearer your_access_token"
```

### Группы

#### Получить список всех групп

```bash
curl -X GET http://127.0.0.1:8000/api/v1/groups/
```

**Ответ:**
```json
[
  {
    "id": 1,
    "title": "Путешествия",
    "slug": "travels",
    "description": "Обсуждение путешествий и туризма"
  }
]
```

#### Получить группу по ID

```bash
curl -X GET http://127.0.0.1:8000/api/v1/groups/1/
```

## Уровни доступа

### Неаутентифицированные пользователи

- ✅ Чтение постов
- ✅ Чтение комментариев
- ✅ Чтение групп
- ❌ Создание/изменение/удаление контента
- ❌ Доступ к эндпоинту `/follow/`

### Аутентифицированные пользователи

- ✅ Чтение всего контента
- ✅ Создание постов и комментариев
- ✅ Изменение и удаление своего контента
- ✅ Подписка на других пользователей
- ✅ Просмотр своих подписок

## Структура проекта

```
api-final-yatube-ad/
├── yatube_api/
│   ├── api/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── __init__.py
│   ├── posts/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   └── __init__.py
│   ├── yatube_api/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __init__.py
│   ├── manage.py
│   └── db.sqlite3
├── tests/
│   ├── fixtures/
│   ├── conftest.py
│   ├── test_comment.py
│   ├── test_follow.py
│   ├── test_group.py
│   ├── test_jwt.py
│   └── test_post.py
├── postman_collection/
│   ├── API_for_yatube.postman_collection.json
│   ├── README.md
│   └── set_up_data.sh
├── requirements.txt
└── README.md
```

## Модели данных

### Post
- `id`: Уникальный идентификатор
- `text`: Текст поста
- `author`: Автор поста (ForeignKey на User)
- `image`: Изображение (опционально)
- `group`: Группа (ForeignKey на Group, опционально)
- `pub_date`: Дата публикации

### Comment
- `id`: Уникальный идентификатор
- `author`: Автор комментария (ForeignKey на User)
- `post`: Пост (ForeignKey на Post)
- `text`: Текст комментария
- `created`: Дата создания

### Group
- `id`: Уникальный идентификатор
- `title`: Название группы
- `slug`: URL-идентификатор
- `description`: Описание группы

### Follow
- `id`: Уникальный идентификатор
- `user`: Пользователь, который подписывается (ForeignKey на User)
- `following`: Пользователь, на которого подписываются (ForeignKey на User)

## Тестирование

### Запуск тестов

```bash
pytest tests/
```

### Запуск конкретного теста

```bash
pytest tests/test_follow.py -v
```

### Использование Postman

1. Импортируйте коллекцию `postman_collection/API_for_yatube.postman_collection.json` в Postman
2. Запустите скрипт подготовки данных: `bash postman_collection/set_up_data.sh`
3. Запустите коллекцию тестов в Postman

## Обработка ошибок

API возвращает стандартные HTTP статус-коды:

- `200 OK`: Успешный запрос
- `201 Created`: Ресурс успешно создан
- `400 Bad Request`: Некорректные данные запроса
- `401 Unauthorized`: Требуется аутентификация
- `403 Forbidden`: Недостаточно прав доступа
- `404 Not Found`: Ресурс не найден
- `500 Internal Server Error`: Ошибка сервера

## Лицензия

Этот проект является учебным проектом и распространяется в образовательных целях.

## Контакты

Для вопросов и предложений обратитесь к разработчикам проекта.
