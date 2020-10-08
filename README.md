# Ocelot - портал для Управляющих компаний #

![]() *тут скриншот*

Система Ocelot позволяет управляющим компаниям (обслуживание жилых домов):

 - вести учёт технического состояния жилого дома;

 - вести суточный/месячный/годовой учёт потребляемых ресурсов (по дому/по квартире);

 - импорт/экспорт данных из файлов *.csv, *.dbf, *.xls, *.xlsx;

 - автоматический анализ показаний приборов учёта с выводом отчёта о причинах возгникновения проблем, и возможных вариантах их решения;

 - поддержака ролей для пользователей и разграничение их прав;

## В репозитории 2 бранча ##

[master](https://github.com/stepanskryabin/ocelot/tree/master) - Основная и стабильная ветка.

[develop](https://github.com/stepanskryabin/ocelot/tree/develop) - Ветка для добавления нового функционала.

## В разработке применяется ##

[Python 3.8](https://www.python.org/) - язык программирования

[Django 3.1](https://www.djangoproject.com/) - основной фреймворк

[Pandas](https://pandas.pydata.org/) -  библиотека для обработки и анализа данных

## Описание репозитория ##

* /portal - директория проекта

* /heat - подсистема работы и анализа показаний приборов учёта

* /pasport - подсистема работы с объектами и их параметрами

* /lk - подсистема работы с аккаунатами пользователей

## Установка ##

Установить [Python](https://www.python.org/downloads/) версии 3.8.

Загрузить и установить последнюю версию [git](https://git-scm.com/downloads).

Если нужен GUI, установить [GitHub Desktop](https://desktop.github.com/).

Настроить Git или GitHub Desktop введя свои `username` и `email` от аккаунта созданного на [github](https://www.github.com).

## Форк репозитория Morelia Server ##

Для того чтобы форкнуть к себе репозиторий Ocelot нужно перейти по [ссылке](https://github.com/stepanskryabin/ocelot/fork).

## Клонирование репозитория на локальный компьютер ##

Клонировать репозиторий к себе на локальный компьютер используя командную строку и `git`

```cmd
git clone https://github.com/{username}/ocelot.git
cd ocelot
```

Переключаемся на ветку develop

```cmd
git checkout develop
```

Синхронизируем свой форк с оригинальным репозиторием `upstream` Ocelot

```cmd
git remote add upstream https://github.com/stepanskryabin/ocelot.git
```

Проверяем появились ли репозиторий `upstream` в списке удалённых репозиториев

```cmd
git remote -v
> origin    https://github.com/{username}/ocelot.git (fetch)
> origin    https://github.com/{username}/ocelot.git (push)
> upstream  https://github.com/stepanskryabin/ocelot.git (fetch)
> upstream  https://github.com/stepanskryabin/ocelot.git (push)
```

При использовании `GitHub` выбрать в меню `File` пункт `Clone repository...` далее следовать инструкциям

## Настройка виртуального окружения Pipenv ##

Для работы с проектом необходима установка библиотек которые он использует, т.н. `рабочее окружение`, для этого используется утилита [Pipenv](https://github.com/pypa/pipenv)

Если не установлен pipenv, выполнить

```cmd
python -m pip install pipenv
```

Создать виртуальное окружение в директории с проектом

```cmd
pipenv shell
```

Установить все требуемые библиотеки из Pipfile

```cmd
pipenv install --ignore-pipfile
```

## Запуск сервера ##

Перед запуском необходимо создать базу данных с пустыми таблицами, командой

```cmd
python ./portal/manage.py migrate
```

Дополнительно можно добавить администратора

```cmd
python ./portal/manage.py createsuperuser
```

Для запуска сервера используйте команду

```cmd
python ./portal/manage.py runserver
```

## Создание пулл-реквеста для внесенния изменений в develop-ветку Ocelot ##

Получение последних изменнений из develop-ветки Ocelot

```cmd
git pull upstream develop
```

Отправка изменений в develop-ветку своего форка

```cmd
git push
```

Для создания пулл-реквеста, необходимо перейти на [GitHub](https://www.github.com), выбрать свой форк и в правом меню нажать на `New pull request`, после чего выбрать бранч из которого будет производится перенос изменений в develop-ветку Ocelot и нажать `Create pull request`.

## Требования к стилю кода ##

Перед началом работы рекомендуется прочитать [PEP 8 - руководство по написанию кода на Python](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html). Обязательно использовать линтер (flake8, pylint или подобный).

## Написание и запуск тестов ##

Для написания тестов используется встроенный модуль Unittest. Тесты расположены в фале tests.py, для каждого приложения свои тесты.

Для запуска тестов выполните:

```cmd
python ./portal/manage.py test
```

## Контакты ##

[Telegram](https://t.me/@stapanskryabin)
