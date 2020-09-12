# def talk(func):
#     def func_decor(word):
#         print('Kod do vizova func')
#         func(word)
#         print('Kod posle vizova func')

#     return func_decor


# @talk
# def foo(word):
#     print(word)


# # foo = talk(foo)

# # foo('Yaaaaaaah')
# foo()

# self.... - dlya klassov

# ______________________________________
# Zamikanie

# def talk():
#     x = 1
#     a = 11

#     def func_decor():
#         # nonlocal a #chtobi izmeniat object v drugoi local tere
#         # a += 1 
#         print(x)
#         print(a)


#     return func_decor

# a = talk()
# print(a.__closure__[0].cell_contents) #kortej => 0 el korteja => preobrazovat v nujni vid
# print(a.__closure__[1].cell_contents)

# a.__closure__[0].cell_contents = 3

# print(a.__closure__[0].cell_contents)

# # print(dir(a)) #Check na atributi
# # __clouser__ vozvraschaet rod atributi



# ______________________________________

# @posledni
# @pervi_decorator
# def foo():
#     pass




# def talk(func):
#     def func_decor(word):
#         print('Kod do vizova func')
#         func(word)
#         print('Kod posle vizova func')
#     func_decor.__doc__ = func.__doc__

#     return func_decor


# @talk
# def foo(word):
#     '''
#     Hello
#     '''
#     print(word)

# a = foo('si')
# print(a.__doc__)




# ______________________________________

import logging


logging.basicConfig(
    filename='app.log',#imya file kuda pichutsa ochibki, inache print in konsol
    format="%(levelname)-10s %(asctime)s %(message)s",#format soobchenia
    level=logging.ERROR#uroven logirovania, logi s kakim urovnem mogut zapisivatsia
)

# log =logging.getLogger('logg')#sozdaem log dlia opr prilojenia; sozdaem object(nazvanie)
# log_app =logging.getLogger('app')
# # host = 'localhost'
# # port = 7777
# # log.critical('cant connect to %s  at port %d', host, port)
# log.critical('cant connect to %s  at port %d', 'localhost', 7777)

# params = {'host':'python',
#         'port':80}
# log_app.error('cant connect to %(host)s at port %(port)d', params)



a = 1
while True:
    a = 7

    if a == 7:
        log.critical('cikl ostanovite')