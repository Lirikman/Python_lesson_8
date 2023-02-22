# 2. Написать свой декоратор

def text_operations(function):
    def wrapper(*args, **kwargs):
        print('Текст в верхнем регистре -', str(args).upper().lstrip('(').rstrip(')'))
        print('Текст в нижнем регистре -', str(args).lower().lstrip('(').rstrip(')'))
        function(*args, **kwargs)
        print('Текст с обратным порядком элементов -', str(args[::-1]).lstrip('(').rstrip(')'))

    return wrapper


@text_operations
def show_text(a, b):
    print('Оригинальный текст:\n', str(a), '\n', str(b))


show_text('ПрИвеТ, КаК ДелА?', 'СпАсиБо, у МеНя ВСЁ отлично!')

# 3. Написать декоратор, замеряющий время выполнение декорируемой функции
import time


def show_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        print('Время выполнения функции:', end - start)

    return wrapper


@show_time
def operations_num(x, y):
    print('Сумма чисел равна:', x + y)
    print('Разность чисел равна:', x - y)
    print('Произведение чисел равно:', x * y)
    print('Частное от деления чисел равно:', x / y)

operations_num(10, 20)


@show_time
def conc_word(a, b, c='Python'):
    list_word = ''
    list_word += str(a)
    list_word += str(b)
    list_word += str(c)
    print('Конкатенация слов -', list_word)


conc_word('I', 'love')


# 4. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
# (создание объектов оформить в виде функций)

def list_num():
    number = [i for i in range(1, 1000000)]
    print('Создание списка с числами от 1 до 1000000')
    return number

start_list = time.time()
list_num()
list_time = time.time()-start_list
print('Время создания списка с числами от 1 до 1000000 -', list_time)
def gen_num():
    number = (i for i in range(1, 1000000))
    print('Создание генератора чисел от 1 до 1000000')
    return number

start_gen = time.time()
gen_num()
gen_time = time.time()-start_gen
print('Время создания генератора чисел от 1 до 1000000 -', gen_time)

if list_time > gen_time:
    print('Генератор чисел создался быстрее списка чисел на ', str(list_time-gen_time), 'сек.')
elif list_time < gen_time:
    print('Список чисел создался быстрее генератора на ', str(gen_time - list_time), 'сек.')
else:
    print('Список чисел и генератор чисел создались за одно и то же время!')