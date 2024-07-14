# 1. num_custom_sequence.py
Программа, которая выводит n первых элементов последовательности 122333444455555… (число повторяется столько раз, чему оно равно)


# 2. Product Store
Тестовое задание для Доктор24 и Сарафан.

Django backend проект магазина продуктов со следующим функционалом:

- реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке

- реализован эндпоинт для просмотра всех категорий с подкатегориями с пагинацией

- реализована возможность добавления, изменения, удаления продуктов в админке
- реализован эндпоинт вывода продуктов с пагинацией
- реализован эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.
- реализован эндпоинт вывода  состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
- реализована возможность полной очистки корзины
- операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь
- операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной
- реализована авторизация по токену


## Технологии:
![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/DJANGO-4.2.13-blue?logo=django&logoColor=white)
![djangorestframework](https://img.shields.io/badge/DJANGORESTFRAMEWORK-3.15.1-blue?logo=django&logoColor=white)
[![Django-Imagekit](https://img.shields.io/badge/DjangoImagekit-blue)](https://django-imagekit.readthedocs.io/)

## Запуск проекта

Клонируйте репозиторий и перейдите в него:
```
git clone https://github.com/Mangekos/grocery_store
cd Product_store
```
Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
Создайте файл .env и поместите туда следующие переменные:
```
SECRET_KEY='your_sercret_key'
ALLOWED_HOSTS=127.0.0.1 localhost
DEBUG=True (при необходимости)
```
Генерировать свой секретный ключ не нужно, в settings.py прописана генерация при запуске проекта.

Проведите миграции:
```
cd grocery_store
python manage.py migrate
```
Запустите проект:
```
python manage.py runserver
```
Для управления через систему администратора создайте superuser:
```
python manage.py createsuperuser
```
### Примеры запросов
Пример GET-запроса для получения списка всех категорий
```
GET /api/categories/
http://127.0.0.1:8000/api/categories/
```
Ответ
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "name": "string",
      "slug": "string",
      "image": "string",
      "sub_categories": [
        {
          "id": 0,
          "name": "string",
          "slug": "string",
          "image": "string"
        }
      ]
    }
  ]
}
```
Пример POST-запроса добавление продукта в корзину
```
POST  /api/shopping_cart/
```
```
{
    "product_id": "0",
    "amount": "1"
}
```
Ответ
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "user": 0,
      "product": 0,
      "quantity": 0
    }
  ]
}
```

##### Весь доступный функционал API:

http://127.0.0.1:8000/api/redoc/

http://127.0.0.1:8000/api/swagger/


### Автор

[Дмитрий Квитковский](https://github.com/Mangekos)
