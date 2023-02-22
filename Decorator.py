# 2. Написать свой декоратор

def text_operations(function):
    def wrapper(*args, **kwargs):
        print('Текст в верхнем регистре - ', str(args).upper().lstrip('(').rstrip(')'))
        print('Текст в нижнем регистре - ', str(args).lower().lstrip('(').rstrip(')'))
        function(*args, **kwargs)
        print('Текст с обратным порядком слов - ', str(args[::-1]).lstrip('(').rstrip(')'))

    return wrapper


@text_operations
def show_text(a, b):
    print('Оригинальный текст:\n', str(a), '\n', str(b))


show_text('ПрИвеТ, КаК ДелА?', 'СпАсиБо, у МеНя ВСЁ отлично!')

import time

# 3. Написать декоратор, замеряющий время выполнение декорируемой функции

def show_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        print('Время выполнения функции:', end - start)

    return wrapper


@show_time
def summ(x, y):
    print(x + y)


summ(10, 20)


def list_sorted(*args):
    temp_list = [args]
    sorted(temp_list)
    return temp_list


list_random = 'Ivan', 'Moscow', 'Sony_Playstation', 'My_name'
print(list_sorted(list_random))