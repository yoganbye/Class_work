# Основы создания веб приложения. Django

# pip freeze - проверка установленных фреймворков
# django-admin startproject <name project> - создать проект в джанго

# manage, asgi, wsgi - предварительно не трогаем

# path('admin/', admin.site.urls)
#      путь в браузере; путь в проекте (вызов)
# ctrl+c - stop консоль

# python3 manage.py runserver <можем указать порт 8080 или ip с портом 0.0.0.0:8080>- запуск сервера
# python3 manage.py startapp core - создать приложение

#_____________________________________________________________________________________________________




#_____________________________________________________________________________________________________
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
    # users = User.objects.filter() - вместо одного объекта, возвращает список объектов
    #user.delete() - удаляет пользователя

    # _______________________________________________________________________
    # python3 manage.py createsupeuser - создаем супер пользователя для работы с админкой
#_____________________________________________________________________________________________________
# User.objects.annotate(param) - добавляет к объекту бд дополнительный параметр
# order_by(поле по которому сортируют) - сортировка



#_____________________________________________________________________________________________________
# Работа с представлениями и шаблонами

# templates папка - для создания шаблонов
# в ней создаем папку с именем приложения(апликейшн)
# {% %} - шаблонизатор для выражений html + py


# <p><a href='/core/posts/{{ post_id }}'>{{ post }}</a></p> ...........href - ссылка

# {% url "post_detail" post.id %}   #post - объект, получаем id


# <p><img alt='post image' src='{{ post.image.url}}' style="width: 450px; height: 450px;"></p>

# alt - сообщение если не будет найдено картинки

# ul - маркированный список
# li - элемент списка
# p - новый абзац
# a - ссылка
# img - картинка


# Для того чтобы отображались картинки нужно:
# в главном url файле
# from Avito import settings
# from django.contrib.staticfiles.urls import static

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#медиа файлы
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#Статические файлы?
#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________

# <form></form> - форма, отправляет данные по опр url; относится к post запросу
# <form action='/post_create' method='post'></form>
# параметры:
# action - путь до стр на который мы хотим отправить наши данные в форме
# method - метод для отправки, чаще post


# {% csrf_token %} - токен для отправки пост запросов в джанго

# core/form - файл для работы с формами джанго

# as_p - оборачиваем каждое поле в тег p



# is_valid() - проверка, соответствуют ли данные отправленные пользователем с теми, что мы ожидаем;
# если фора валидна, то функции вывал true

# form.save(commit=False) - создастся объект на основе изменений, но в базу объект не зальется


# dispatcch - определяет какой метод возвращает/принимает view, dispatcch содержит в себе объект?
#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________

# AUTH_USER_MODEL = 'core.User' - модель для аутентификации

# <article></article> - какой-то блок

# python manage.py test core

# python manage.py collectstatic

# pythonanywhere
#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________

