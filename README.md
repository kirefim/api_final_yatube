## Описание проекта:

Данный проект представляет собой простой API к Yatube.
Позволяет делать запросы к эндпоинтам и получать сериализованные ответы.

#### _Доступные эндпоинты:_

Получение всех публикаций и получение/создание/обновление/удаление публикации с `{post_id}`:
- /api/v1/posts/
- /api/v1/posts/`{post_id}`/

Получение всех групп или конкретной группы с `{group_id}`:
- /api/v1/groups/
- /api/v1/groups/`{group_id}`/

Получение всех комментариев к публикации с `{post_id}` и
получение/создание/обновление/удаление комментария к данной публикации с `{comment_id}`:
- /api/v1/posts/`{post_id}`/comments/
- /api/v1/posts/`{post_id}`/comments/`{comment_id}`/

Подписка на автора публикации
- /api/v1/follow/

Управление токенами аутентификации JSON Web Token:
- /api/v1/jwt/create/
- /api/v1/jwt/refresh/
- /api/v1/jwt/verify/
## Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone https://github.com/kirefim/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv env
source env/bin/activate
```

Обновляем pip до актуальной версии:

```sh
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```sh
pip install -r requirements.txt
```

Перейти в репозиторий проекта yatube_api и накатить миграции:

```sh
cd yatube_api
python3 manage.py migrate
```

Запустить проект:

```sh
python3 manage.py runserver
```
