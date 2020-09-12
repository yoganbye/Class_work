# Настройка виртуального окружения:
# python3 -V
# python3 -m venv env - создалась папка с виртуальным окружением

# Вход в виртуальное окружение:
# Linux:
# # source env/bin/activate

# Windows:
# cd env
# cd Scripts
# activate.bat

# python3 -m pip install django - установка django внутрь виртуального окружения


# ____________________________________________________________________________________
# QuerySet - список с объектами, который имеет всякие методы

# если используем imageField нужна библиотека Pillow
# python3 -m pip install Pillow
# python3 manage.py makemigrations - создаем миграцию, но прежде в instalse добавляем к INSTALLED_APPS  папку приложения(core)
# Если меняем модели, то необходимо делать миграцию заново для того чтобы обновились таблицы в БД

# python3 manage.py migrate - приминение миграции, т.е. создались таблицы в БД на основе классов
# python3 manage.py shell - консоль Djano; в которой можем "играть" с моделями
    # from core.models import Profile
    # from django.contrib.auth.models import User - импорт модели
    # user = User.objects.create(email='root@root.com') - создаем объект юзер
    # users = User.objects.all() - получаем все записи о юзерах
    # users
    # user.username = 'root' - изменяем значение поля пользователя; в модели юзера есть значения, который мы и задем
    # user.save() - сохраняем
    # user - выводит юзера
    # users = User.objects.get(username='global') - запрос в БД с определенными параметрами
    # users = User.objects.filter() - 
    #user.delete() - удаляет пользователя

    # _______________________________________________________________________
    # python3 manage.py createsupeuser - создаем супер пользователя для работы с админкой

