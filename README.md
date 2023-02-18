# DjangoCountries

# Инструкция по развертыванию проекта

1. `python3 -m venv django_venv` - создание venv
2. `django_venv/Script/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py loaddata countries.json`
6. `python manage.py runserver`

## Запуск терминала в контексте django

`python manage.py shell_plus --ipython`

## Статус выполнения заданий

#### Модуль-1

| Задание                                                                                                                              | Статус   |
|--------------------------------------------------------------------------------------------------------------------------------------|----------|
| Создайте новый проект DjangoCountries.                                                                                               | Выполнен |
| Главная страница должна быть доступна по корневому url’у. На ней разместите произвольное приветствие c минимальным HTML оформлением. | Выполнен |
| Запустите проект и проверьте отображение главной страницы.                                                                           | Выполнен |
| Загрузите ваш проект на GitHub                                                                                                       | Выполнен |


#### Модуль-2

| Задание                                                                                                                                                                                                                                | Статус   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Оформите главную страницу в виде полноценного html-документа                                                                                                                                                                           | Выполнен |
| Список с данными для стран возьмите тут.                                                                                                                                                                                               | Выполнен |
| По url: /countries-list/ отобразите нумерованный список всех стран, отобразив в списке только названия стран.                                                                                                                          | Выполнен |
| Загрузите ваш проект на GitHub                                                                                                                                                                                                         | Выполнен |
| Название каждой страны сделайте гиперссылкой, которая ведет на персональную страницу данной страны. На персональной странице страны отобразите ее название(в виде заголовка) и список всех языков, на которых говорят в данной стране. | Выполнен |
| На главной странице добавьте еще одну ссылку “Языки”. По ссылке отобразите страницу со списком всех языков на котором говорят во всех странах.                                                                                         | Выполнен |


#### Модуль-3

| Задание                                                          | Статус   |
|------------------------------------------------------------------|----------|
| Создайте модель-класс Country.                                   | Выполнен |
| Перенесите все страны из исходного json файла в базу данных(БД). | Выполнен |
| Измените работу вашего приложения на работу с БД                 | Выполнен |
| Выгрузите данные из БД в фикстуру(fixture) countries.json        | Выполнен |


#### Модуль-4

| Задание                                                                                                                                      | Статус   |
|----------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Используя информацию с занятия, измените структуру БД, реализовав связь “многие-ко-многом” для стран и языков.                               | Выполнен |
| Добавьте в проект файл requirements.txt                                                                                                      | Выполнен |
| Добавьте в проект файл README.md, добавив в него: информацию о запуске проекта после клонирования и список всех заданий, пометив выполненные | Выполнен |




