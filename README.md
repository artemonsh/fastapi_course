# Курс по FastAPI от Артёма Шумейко
### [Ссылка на YouTube курс](https://www.youtube.com/playlist?list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS)  

В курсе создается каркас веб-приложения для трекинга своего портфеля в Тинькофф Инвестициях.

Библиотеки, планирующиеся к использованию: alembic, sqlalchemy, fastapi-users, fastapi-cache, celery, redis, jinja.

Технологии: аутентификация пользователей (fastapi-users), кэширование запросов (redis), отложенные задачи (celery + redis), тестирование (pytest).

Фронтенд: react (в этом курсе не разбирается).

## Расширенный курс по FastAPI
### [Ссылка на расширенный курс по FastAPI](https://artemshumeiko.ru/?utm_source=github&utm_medium=organic&utm_campaign=fastapi_course)

Если вам хочется глубже познакомиться с FastAPI, а также научиться работать с  
- Асинхронной SQLAlchemy
- Кастомная аутентификация и авторизация
- Redis
- Celery
- Docker
- Nginx (и деплоить свое приложение на реальный сервер)
- Логирование
- Мониторинг

То я приглашаю вас на свой курс. На него записано уже больше 150 человек.
Развернутые отзывы можно прочитать [здесь](https://stepik.org/course/153849/reviews).

## Список уроков
0. [Зачем учить FastAPI](https://youtu.be/7IdfnjXsdN4)
1. [Установка и запуск](https://youtu.be/G0pcbxMsiec)
2. [Эндпоинты, Параметры Пути и Запроса](https://youtu.be/O627QJxlFko)
3. [Валидация данных с Pydantic](https://youtu.be/06l4r-p-qfU)
4. [Базы данных и миграции Alembic](https://youtu.be/hO7b4yh-Qfs)
5. [Регистрация и Авторизация Пользователей](https://youtu.be/nfueh3ei8HU)
6. [Роутеры и Файловая Структура](https://youtu.be/1Ag3RoOjNI0)
7. [Проектирование REST API](https://youtu.be/-RLXmoQ7iSE)
8. [Кэширование через redis](https://youtu.be/t4H25XJG0Uc)
9. [Фоновые задачи с Celery, Redis и Flower](https://youtu.be/fm4LTvMyiwE)
10. [Тестирование API с pytest и pytest-asyncio](https://youtu.be/4xJGQKfN3ZM)
11. [Связываем Фронт и Бэк: CORS и Middleware](https://youtu.be/h0eTzi5Geo8)
12. [Верстка с Jinja. Как украсить API](https://youtu.be/AKLzDJ6XLCc)
13. [Вебсокеты (онлайн-чат)](https://youtu.be/uWSdWJEFd0Y)
14. [Depends зависимости](https://youtu.be/qvzQWBEBHYw)
15. [Docker и Docker Compose](https://youtu.be/_1H1qsNqxwM)
16. [Деплой приложения](https://youtu.be/OxE2UGHPOA0)

## Дополнительно
- [Луковая Архитектура на FastAPI](https://youtu.be/8Im74b55vFc)

## Инструкция
Для локального тестирования необходимо создать виртуальное окружение командой `python3 -m venv venv` и активировать его. Команда `venv\Scripts\activate.bat` - для Windows; `source venv/bin/activate` - для Linux и MacOS.

Затем необходимо перейти в папку с нужным уроком и установить зависимости командой `pip install -r requirements.txt`.

Затем необходимо перейти в папку `src` командой `cd src` и запустить команду `uvicorn main:app --reload` для запуска сервера `uvicorn`. 

После этого можно зайти в браузере по адресу `http://localhost:8000/docs` для просмотра доступных эндпоинтов.

## История звездочек от вас

[![Star History Chart](https://api.star-history.com/svg?repos=artemonsh/fastapi_course&type=Date)](https://star-history.com/#artemonsh/fastapi_course&Date)
